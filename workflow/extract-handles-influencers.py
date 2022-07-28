import time
from multiprocessing import Process, Value, Manager

class Verbose:
    def __init__(self, start_with="", max_lines=25, time_mode="average", average_length=10, round_to=2, show_time=True, line_char="=", space_char="-", arrow_head=">"):
        self.start_with = start_with
        self.max_lines = max_lines
        self.process_time = 0
        self.previous_time = 0
        self.time_mode = time_mode
        self.average_length = average_length
        self.time_steps = [0] * average_length
        self.average_counter = 0
        self.show_time=show_time
        self.round_to = round_to
        self.line_char = line_char
        self.space_char = space_char
        self.arrow_head = arrow_head
    
    def calc_last_time(self):
        current_time = time.time()
        if self.time_mode == "per_step":
            self.process_time = round(current_time - self.previous_time, self.round_to)
        else:
            average = sum(self.time_steps)/self.average_length
            actual_time = round(current_time - self.previous_time, self.round_to)
            self.process_time = round(average, self.round_to)
            self.time_steps[self.average_counter] = actual_time if not actual_time > 100000 else 0.00
            self.average_counter += 1
            if self.average_counter == self.average_length:
                self.average_counter = 0
        self.previous_time = current_time

    def reset_time(self):
        self.process_time = 0

    def make_verbose(self, done, total, start_with="", extra_string=""):
        if start_with == "":
            start_with = self.start_with

        num_lines = int((done/total)*self.max_lines)
        lines = self.line_char*num_lines
        spaces = self.space_char*(self.max_lines-num_lines)

        if self.show_time:
            self.calc_last_time()
            remaining_steps = total - done
            remaining_time = ""
            remaining_time = int(self.process_time * remaining_steps)
            print(f"\r{start_with}  [{lines}{self.arrow_head}{spaces}]  {done}/{total} ETA: {remaining_time} sec for {self.process_time} sec/steps {extra_string}", end="", sep=" ", flush=True)
            if remaining_steps == 0: 
                self.reset_time()
        else:
            print(f"\r{start_with}  [{lines}{self.arrow_head}{spaces}]  {done}/{total} {extra_string}", end="", sep=" ", flush=True)


def divide_chunks(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]

common_verbose = Verbose()
def mp_verbose(finish, length):
    common_verbose.make_verbose(finish, length)


def job(function, inputs, output_list, p_id, worker_states, length, target, finished, halt, graph):
    current_target = 0
    while target.value < length:
        if worker_states[p_id] == True:
            if not halt.value == 1:
                current_target = target.value
                target.value += 1
                target_input = inputs[current_target]
                try:
                    output_value = function(target_input)
                    output_list[current_target] = output_value
                except:
                    pass
                finished.value += 1
                if graph:
                    mp_verbose(finished.value, length)
        else:
            worker_states[p_id] = True
            current_target = p_id

import time

def map_parallel(function, input_list, workers=2, graph=True):
    manager = Manager()
    length = len(input_list)
    
    output_list = manager.list([None] * length)
    state = manager.list([False] * workers)
    processes = []

    target = Value('i', 0)
    finished = Value('i', 0)
    halt = Value('i', 1)

    print("starting processess")
    for i in range(workers):
        process = Process(target=job, args=(function, input_list, output_list, i, state, length, target, finished, halt, graph))
        process.start()
        processes.append(process)
    
    print("processes started")
    time.sleep(1)

    while finished.value < length:
        halt.value = 0 if not False in state else 1
    
    _output = list(output_list)
    
    manager._process.terminate()
    manager.shutdown()
    print()
    return _output