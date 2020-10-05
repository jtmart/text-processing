import pandas as pd
from os import listdir
from multiprocessing import Process, Value, Manager
from time import time


def runScript(name, p_num, t_nodes, f_list, input_path, no_files, cumulative):
    print("Starting ", name)
    target = p_num
    del [p_num]
    while target < len(f_list):
        try:
            i_file_path = input_path + f_list[target]
            final_string = ""
            with open(i_file_path) as file:
                for line in file:
                    final_string += line
                file.close()

            # final_string.replace("\n")
            to_add = {"text": final_string}
            # print(to_add)
            cumulative[0] = cumulative[0].append(to_add, ignore_index=True)

        except Exception as e:
            print(name, "error -> ", e.__str__())

        no_files.value -= 1
        target += t_nodes
        print(name, ": files left", no_files.value)


if __name__ == "__main__":
    start_time = time()
    input_folder = r"./txt_input/"  # write your input folder here (DON'T FORGET TO PUT / AT THE END)
    output_file_name = r"test"  # write your output file name here without the extension like ".csv" or ".xlsx"
    file_type = "xl"  # csv = csv & xl = excel file
    df = pd.DataFrame(columns=["text"])
    template = Manager().list([df])
    fileList = listdir(input_folder)
    if len(fileList) <= 0:
        print("input folder has nothing in it. please check if you have entered correct input folder path" +
              " and rerun this script")
    else:
        nodes = int(input("how many processing units?? : "))
        no_of_files = Value("i", len(fileList))
        processes = []
        for i in range(0, nodes):
            process_name = "PROCESS " + str(i + 1)
            process = Process(target=runScript, args=(process_name, i, nodes, fileList, input_folder,
                                                      no_of_files, template))
            process.start()
            processes.append(process)
        for process in processes:
            process.join()
        if file_type == "csv":
            template[0].to_csv(output_file_name + ".csv", index=False, encoding="UTF-8")
        else:
            template[0].to_excel(output_file_name + ".xlsx", sheet_name="sheet1", index=False, encoding="UTF-8")

    print("time taken: ", ((time()-start_time)/60)/60, "hrs")
