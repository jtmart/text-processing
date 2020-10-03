from os import listdir
from os import mkdir
import multiprocessing
from multiprocessing import Value
import pandas as pd
from multiprocessing import Manager


def RunScript(name, p_num, t_nodes, f_list, input_path, no_files, cumulative):
    print("Starting ", name) #put the script into the parent folder of the "outputs" folder (e.g. "_temp")
    target = p_num
    del[p_num]
    while target < len(f_list):
        try:
            i_file_path = input_path + f_list[target]
            df = pd.read_csv(i_file_path, engine='python', sep=',')
            del[i_file_path]
            for i in range(0, len(df.country)):
                if str(df.country[i]) != "india":
                    df = df.drop([i], axis=0)

            cumulative[0] = pd.concat([cumulative[0], df])
            no_files.value -= 1
            target += t_nodes
            print(name, ": files left", no_files.value)
        except Exception as e:
            print(name, ": seems like a prob -> ", e.__str__())


if __name__ == "__main__":
    template = Manager().list([pd.read_csv(r"./_temp/template.csv")]) #folder wheter CSVs are stored, original in linux "./_temp/template.csv"
    input_dir = r"./_temp/clear_india/"
    output_dir = (str(input("what should i call the output dir??: \n")))
    output_dir = r"./" + output_dir
    try:
        mkdir(output_dir)
    except:
        print("directory already exists, so I will write the file in there \n")

    print("THE THE FILE WILL BE SAVED AS 'only_india.csv'")
    output_dir += r"/only_india.csv" #check is this file is there
    fileList = listdir(input_dir)
    while True:
        if len(fileList) <= 0:
            print("no files found in ", input_dir, "\n")
            input_dir = str(input("please enter a new dir: "))
            input_dir = r"./" + input_dir + "/"
            fileList = listdir(input_dir)
        else:
            break

    nodes = int(input("how many processing units?? : "))
    no_of_files = Value("i", len(fileList))
    processes = []
    for i in range(0, nodes):
        process_name = "PROCESS " + str(i+1)
        process = multiprocessing.Process(target=RunScript, args=(process_name, i, nodes, fileList, input_dir,
                                                                  no_of_files, template))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    template[0].drop([0], axis=0).to_csv(output_dir, index=False)