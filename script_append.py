
import os.path
# ans=list()
import numpy as np
import pandas as pd
csv_file=pd.read_csv("metadata.csv")
# csv_file=csv_file.to_numpy()
csv_file['data']=""
print (csv_file)

for filename in os.scandir():
	# file=str(filename)
	if (filename.path.endswith('.txt')):
		f=filename.name
		print (f)
		with open(f, 'r',  encoding="utf8") as myfile:
			data = myfile.read()
		f=f[:15]
		print (f)
		for i in range(len(csv_file)):

			if (csv_file.loc[i,'id']==f):
				csv_file.loc[i,'data']=data
	else:
		print ("notfound")

# np.savetxt("new_csv.txt", csv_file, delimiter=",", fmt='%s')
csv_file.to_csv('output.csv', index=False)