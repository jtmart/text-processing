import os

count = 0
for dirpath, dnames, fnames in os.walk("./"):
	for f in fnames:
		try:
			# print(f, len(f))
			file = open(f)
			text = file.read()
			file.close()
			if "" in text:
				print(f)
				count += 1
				print("boo")
			# text = text.replace("","")
			# file = open(f,"w")
			# file.write(text)
			# file.close()
		except:
			pass
			# print(f)
			# count += 1
print(count)

# file = open("wrong.txt")
# text = file.read().split('\n')[:-1]
# file.close()

# for f in text:

# 	file = open(f)
# 	t = file.read()
# 	file.close()