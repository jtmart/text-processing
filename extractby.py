#‘path_txt’ is the where you have all your text files (say 100 text files).
#‘path_csv’ is where you’ve saved a CSV that lists the text files names that need to be combined (say text files with names as: “ABC”, “DEF”, #“GHI”, from the 100 total files).

#‘path_save’ is where the final combined file will be saved

import pandas as pd

 

path_txt = r"./data/pms_modi/"

path_csv = r"./csv/meta2.csv"

path_save = r"output/cumulative outputs/output_2.txt"

 

Ids = pd.read_csv(path_csv).ID

Output = open(path_save, "wb")

for path in Ids:

    path_txt_new = path_txt + path + ".txt"

    File = open(path_txt_new, "rb")

    Output.writelines(File.readlines())