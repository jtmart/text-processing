f = open('nehru.txt', 'r')

lines = f.readlines()

ans = 314
newf = open('e'+(4-len(str(ans)))*'0'+str(ans)+".txt", 'w')
for i in range(len(lines)):
	if(lines[i][:4] == "****"):
		ans+=1
		newf.close()
		newf = open('e'+(4-len(str(ans)))*'0'+str(ans)+".txt", 'w')
		continue
	newf.write(lines[i])

print(ans)

f.close()
