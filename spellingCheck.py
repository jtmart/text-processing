file = open("words.txt")
words = file.read().split('\n')[:-1]
file.close()

file = open("t19840918670337.txt")
text = file.read().split()[:-1]
file.close()

for i in range(len(words)):
	words[i] = words[i].lower()

for i in range(len(text)):
	text[i] = text[i].lower()

for c in text:

	while(c!="" and (c[-1] < 'a' or c[-1] > 'z')):
		c = c[:-1]

	if c not in words:
		print(c)
		words.append(c)

# text = "\n".join(words)
# text += "\n" + words[-1] 
# file = open("words.txt","w")
# file.write(text)
# file.close()