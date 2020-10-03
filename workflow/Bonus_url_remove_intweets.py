import re
from os import listdir
from os import mkdir
import multiprocessing
from multiprocessing import Value, freeze_support
#All the text files should be inside a 'txt' folder / the txt folder should be inside "_temp"
#The countdown when processing files is 0 only if using one thread

def RunScript(name, p_num, t_nodes, f_list, input_path, output_path, no_files):
    print("Starting ", name)
    target = p_num

    while target < len(f_list):
        in_path = input_path + f_list[target]

        try:
            print(name, ": ", in_path)
            with open(in_path, mode="r", encoding="UTF-8") as file:
                lines = []
                for line in file:
                    line = line.replace("www", "http://www")
                    instances = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
                    for url in instances:
                        line = line.replace(str(url), "")
                    lines.append(line)
                file.close()
                if output_path != ".":
                    out_path = output_path + f_list[target]
                    with open(out_path, "w", encoding="UTF-8") as o_file:
                        o_file.writelines(lines)
                        o_file.close()
                    del[out_path]
                else:
                    with open(in_path, mode="w", encoding="UTF-8") as file_write:
                        file_write.writelines(lines)
                        file_write.close()
            del[in_path]
        except Exception as e:
            print(e.__str__())
        
        target += t_nodes
        no_files.value -= 1
        print(name, ": files left ", no_files.value)


if __name__ == "__main__":
    freeze_support()
    input_dir = "./_temp/txt/"
    output_dir = "."

    fileList = listdir(input_dir)
    while True:
        if len(fileList) <= 0:
            print("no files found in ", input_dir, "\n")
            input_dir = str(input("please enter a new dir: "))
            input_dir = "./" + input_dir + "/"
            fileList = listdir(input_dir)
        else:
            break

    nodes = int(input("how many processing units?? : "))
    no_of_files = Value('i', len(fileList))
    processes = []
    for i in range(0, nodes):
        process_name = "PROCESS " + str(i+1)
        process = multiprocessing.Process(target=RunScript, args=(process_name, i, nodes, fileList, input_dir,
                                                                  output_dir, no_of_files, ))
        process.start()
        processes.append(process)
    for process in processes:
        process.join()

    input("process finished, enter anything to terminate this window")
