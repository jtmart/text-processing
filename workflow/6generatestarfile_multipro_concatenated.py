# author: Vedant Jumle
from os import listdir

input_path = r"./all_output/" # your input folder path here
output_path = r"./" # your output folder path here

filelist = listdir(input_path)
file_amount = len(filelist)
with open(output_path + "cumulative_output.txt", 'w', encoding="utf-8") as output_file:
    for filename in filelist:
        with open(input_path + filename, 'r', encoding="utf-8") as input_file:
            lines = []
            for line in input_file:
                lines.append(line)

            output_file.writelines(lines)
            input_file.close()

        file_amount -= 1
        print("files left", file_amount)

    output_file.close()

print("process finished")