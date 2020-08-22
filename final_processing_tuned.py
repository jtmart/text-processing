import pandas as pd
import os

dataf = pd.read_csv("metadata.csv") #csv file
txt_files_to_be_removed=[] #script needs to be inside the folder which has txt files and metadata

year_to_be_removed=['independencerepublicday'] # WHAT IS TO BE REMOVED year_to_be_removed does not matter if numerical: [1916,1917] , if string ['nehru','gandhi']
index_to_be_removed=[]
for i in range(len(dataf)):
	if(dataf.iloc[i,12] in year_to_be_removed):  #in python, column numbers start with 0. [i,2] matlab column 3 in the CSV
		txt_files_to_be_removed.append(dataf.iloc[i,0])
		index_to_be_removed.append(i)
print(txt_files_to_be_removed)
print(index_to_be_removed)
dataf.drop(index=index_to_be_removed,inplace=True)
dataf.reset_index(drop=True,inplace=True)
#print(dataf)
dataf.to_csv("new_combined.csv",encoding="utf-8") #it does need alternative encoding

fin=[]
for i in range(len(txt_files_to_be_removed)):
	fin.append(txt_files_to_be_removed[i] + ".txt")

for i in fin:
	os.remove(i)


