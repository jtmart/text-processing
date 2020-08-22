import os

# path to corpus folder
path = './11pmos_Final1'

n = int(input("Enter minimum limit for characters in a word: "))

words = []

for r,d,f in os.walk(path):
	for file in f:

		fd = open(path + '/' + file,'r')
		text = fd.read().split()
		fd.close()


		for word in text:

			if len(word) >= n:
				words.append(word)

words = list(set(words))

string = ""
for word in words:
	string += word + '\n'

file = open("WordList.txt",'w')
file.write(string)
file.close()