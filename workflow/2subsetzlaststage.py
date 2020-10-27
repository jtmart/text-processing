from pandas import DataFrame, read_csv

input_csv = r"new_combined.csv" # write your CSV file name here like -> "my csv file.csv"
input_folder = r"./Combined_utf8_selection/" # write your folder name here like -> "./<my input folder>/"
output_folder = r"./Combined_utf8_selection_output2/" # write your output folder here like -> "./<my output folder>/"
copyList = read_csv(input_csv).id



for id in copyList:
    try:
        with open(input_folder + str(id) + ".txt", "r") as file:
            with open(output_folder + str(id) + ".txt", "w") as out_file:
                out_file.writelines(file)

    except:
        print("no such file in the folder: ", str(id) + ".txt")