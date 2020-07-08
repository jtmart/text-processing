import pandas as pd
import yaml 
import csv
import re


def remove_null(alist):
	#Removes null from lists
	blist = []
	for val in alist:
		if pd.isna(val) == False:
			blist.append(val)
	return blist 

def make_not_columns(nflevels, levels):
	#Gives the rows which are to be dropped
	not_rows  = []
	for i in range(1,nflevels + 1):
		if i not in levels:
			not_rows.append(i - 1)
	return not_rows

def make_dictionary(levelType, filename = "variables.yml",file_to_read = "variables.csv"):
	#---------------------------
	df = pd.read_csv(file_to_read)
	df = df.T
	(nfrows,nfcolumns) = df.shape
	#---------------------------
	#Preprocessing
	rows = []
	for i in range(nfrows):
		row = df.iloc[i]
		row = remove_null(row)
		rows.append(row) 
	#---------------------------

	for i in range(len(rows)):

		if levelType == 1:
			rows[i][2] = rows[i][0]
		elif levelType == 2:
			rows[i][2] = rows[i][1]

		rows[i] = rows[i][2:]

	headers = {}
	headers_count = 1
	links = {}

	i = 0
	while(i < nfrows):

		array = rows[i]
		casetype = rows[i+1]

		i += 2

		if(len(array) <= 1):
			continue

		if array[0] not  in headers:
			headers[array[0]] = headers_count
			headers_count += 1

		for j in range(1,len(array)):
			word = array[j]
			case = casetype[j]

			num = headers[array[0]]

			if word not in links:
				links[word] = [num]
			else:
				if num not in links[word]:
					links[word].append(num)
			
			if case == 'nc':
				if 'A' <= word[0] <= 'Z':
					word = word[0].lower() + word[1:]
				else:
					word = word[0].upper() + word[1:]
				
				if word not in links:
					links[word] = [num]
				else:
					if num not in links[word]:
						links[word].append(num)

	string = "%\n"
	for i in headers:
		string += str(headers[i]) + '\t' + i + '\n'
	string += '%\n'

	for word in links:
		string += word
		arr = links[word]
		for num in arr:
			string += '\t' + str(num)
		string += '\n'
	
	file = open('LIWC.dic','w')
	file.write(string)
	file.close()

n = int(input("what level do you wanna make the header [1/2/3] = "))
make_dictionary(n)