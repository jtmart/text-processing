import os
all_files = []
for filename in os.listdir("vp_singh_nirav"):
	all_files.append(filename)
d = [] 
with open("all_vpsingh.txt") as file:
	lines = file.readlines()
	count = 0
	for line in lines:
		count += 1
		line = line.strip("\n") + ".txt"
		d.append(line)
		print(line,os.path.exists("vp_singh_nirav/" + line))
	print(count)
print("-----------------------")
for f in all_files:
	if f not in d:
		print(f)