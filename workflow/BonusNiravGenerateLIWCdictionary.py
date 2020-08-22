import pandas as pd
import yaml 
import csv
import re
import warnings
import os
warnings.filterwarnings("ignore")

def make_list(alist):
	#Removes null from lists
	blist = []
	for val in alist:
		blist.append(val)
	return blist 

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

def make_and_think(js,arr,level):
	#Forms the basic structure of json
	if level ==  len(arr) - 1:
		if arr[level] not in js:
			js[arr[level]] = []
	elif arr[level] not in js:
		js[arr[level]] = {}
		make_and_think(js[arr[level]],arr,level + 1)
	else:
		make_and_think(js[arr[level]],arr,level + 1)
	return js

def make_liwc(dict_levels,arr):
	global head_count
	global all_items
	global all_headings
	item_arr = []
	for key in dict_levels:
		if key not in all_headings:
			all_headings[key] = head_count
			if head_count not in item_arr:
				item_arr.append(all_headings[key])
			head_count += 1
		else:
			item_arr.append(all_headings[key])
	for item in arr:
		if item in all_items:
			for number in item_arr:
				if number not in all_items[item]:
					all_items[item].append(number)
		else:
			all_items[item] = []
			for number in item_arr:
				if number not in all_items[item]:
					all_items[item].append(number)

def makeliwc_comp(filename):
	global head_count
	global all_items
	global all_headings
	with open(filename,"a") as file:
		file.write('%\n')
		for key in all_headings:
			file.write(str(key) + "\t" + str(all_headings[key]) + "\n")
		file.write('%\n')
		for key in all_items.keys():
			file.write(str(key) + "\t")
			for number in range(len(all_items[key])):
				if number == len(all_items[key]) - 1:
					file.write(str(all_items[key][number]) + "\n")
				else:
					file.write(str(all_items[key][number]) + "\t")


def make_and_put(js,arr,value,level):
	#Adds an array is the json as value for the pair arr[len(arr) - 1] 
	if level == len(arr)-1:
		if arr[level] in js:
			assert(isinstance(js[arr[level]],list))
			for v in value:
				js[arr[level]].append(v)
	if arr[level] in js and level != len(arr)-1:
		make_and_put(js[arr[level]],arr,value,level + 1)
	return js

def check_script(filename = "dictionary.yml"):
	non_utf_8_pattern = "\\\\x"
	with open(filename, 'rb') as stream:
		data = stream.read()
		data = data.decode("utf-8","backslashreplace")
		z = re.match(non_utf_8_pattern, data)
		if z:
			print((z.groups()))
		else:
			pass
			#print("NO MATCH FOUND")


def rem_utf_8(filename,filename2):
	non_utf_8_pattern = "\\\\x"
	with open(filename, 'rb') as stream:
		data = stream.read()
		data = data.decode("utf-8","backslashreplace")
		z = re.match(non_utf_8_pattern, data)
		#print(data)
		data = re.sub("\\\\x92","\'",data)
		data = re.sub("\\\\x96","-",data)
		data = re.sub("\\\\x97","—",data)
		data = re.sub("\\\\xf3","ó",data)
		print(data)
		with open(filename2, 'w+') as file:
			file.write(data)

def make_dictionary(nflevels = 6,levels = [1,2,3,4,5],filename = "dictionary.yml",file_to_read = "dictionary.csv",liwc_filename = "dictionary.dic"):
	#---------------------------
	df = pd.read_csv(file_to_read)
	levelsdropped = make_not_columns(nflevels,levels)
	df = df.drop(levelsdropped)
	nflevelsdropped = len(levelsdropped)
	levels_remaining  = nflevels - nflevelsdropped
	#print("levels_remaining = ",levels_remaining)
	df = df.T
	(nfrows,nfcolumns) = df.shape
	#---------------------------
	#Preprocessing
	rows = []
	for i in range(nfrows):
		row = df.iloc[i]
		#if i % 2 == 0:
		row = make_list(row)
		rows.append(row) 
	#---------------------------
	#print("Rows = ",rows)
	#Make Json
	js = {}
	for row_no in range(0,len(rows) - 1,2):
		row = rows[row_no]
		c_row = rows[row_no + 1]
		level = 0
		dict_levels = row[:levels_remaining]
		make_and_think(js,dict_levels,0)
		arr = []
		for item_no in range(levels_remaining,len(row)):
			#print("Item_no = ",item_no)
			item = row[item_no]
			if pd.isna(item) == False:
				item = item.strip()
				item = re.sub("\\\\x92","\'",item)
				item = re.sub("\\\\x96","-",item)
				item = re.sub("\\\\x97","—",item)
				item = re.sub("\\\\xf3","ó",item)
				#item = str(item,'utf-8')
				#print("Item = ",item)
				if c_row[item_no] == "nc":
					if item == item.lower():
						arr.append(item)
						arr.append(item[0].capitalize() + item[1:])
					else:
						arr.append(item)
						arr.append(item.lower())
				else:
					arr.append(item)
			else:
				pass
				#print("Null Item Here")
		make_liwc(dict_levels,arr)
		make_and_put(js,dict_levels,arr,0)
	#---------------------------------------
	#DUMP Json onto yml file and liwc
	makeliwc_comp(liwc_filename)
	ff = open("temp.yml", 'w+')
	yaml.dump(js,ff,allow_unicode = True,default_flow_style = False)
	rem_utf_8("temp.yml",filename)
	ff.close()
	os.remove("temp.yml")

all_headings = {}
all_items = {}
head_count = 1

make_dictionary()
