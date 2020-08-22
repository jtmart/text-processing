import os

long_words = open("long_words2.txt", "r").read().split("\n")
for i in range(len(long_words)):
    long_words[i] = long_words[i][:-1]

for file_name in os.listdir("corpus"):
    file_path = os.path.join("corpus", file_name)

    file = open(file_path, encoding='utf-8', errors='replace')
    fileContent = file.read()
    file.close()

    for word in long_words:
        fileContent = fileContent.replace(word, " LONG_WORD ")
    file = open(file_path, "w", encoding="utf-8")
    file.write(fileContent)
    file.close()
    print(file_name)
