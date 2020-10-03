#let me clarify again. 
#The 'Name' stands for the text file name. So text files will be named as what is written under 'Name'.
#The 'Translation' stands for the text. So the content under 'Translation' will be saved as the text inside the files.

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
path_input = r"file.csv" #the name of the original csv, often metadata.csv
path_save = r"./output/" #create an empty folder called output

csv = pd.read_csv(path_input) #csv inside folder

Ids = csv.Name  #name of the column where the text ids are (id column, t numbers in metadata.csv)

for i in range(0, len(Ids)):
    save_as = path_save+Ids[i]+".txt"
    Output = open(save_as, "w", encoding="UTF-8")
    Output.writelines([csv.Translation[i]]) #name of the column where the text of the speeches/tweets are (usually last column of metadata.csv)