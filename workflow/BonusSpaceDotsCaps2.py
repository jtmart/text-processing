import re
from os import listdir

input_folder = r"./textfiles/utf8/"
fileList = listdir(input_folder)

counter = len(fileList)
for file_name in fileList:
    filePath = input_folder + file_name
    with open(filePath, "r", encoding="UTF-8") as file:
        lines = []
        for line in file:
            matches = re.findall(r"[.]\w", line)
            for match in matches:
                line = line.replace(match, match[0] + " " + match[1])
            try:
                sub_str = line[0] + line[1] # + line[2]
                matches_2 = re.findall(r"\s[A-Z]", str(sub_str))
                line = line.replace(matches_2[0], matches_2[0][1], 1)
            except:
                i=0
                del[i]

            lines.append(line)

        # print(lines)
        file.close()
        with open(filePath, "w", encoding="UTF-8") as new_file:
            new_file.writelines(lines)
            new_file.close()
    counter -= 1
    # break
    print("files left: ", counter)

print("processed finished")
