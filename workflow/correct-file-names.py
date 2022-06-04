import csv
import os
from csv import writer


rows=[]
with open('new_sample.csv','r',encoding='utf8') as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)

print(len(rows))

ids=[]
find=[]
txt=[]
file=[]
uqid=[]
nl=[]
for i in range(1,len(rows)):
    nl.append(rows[i][0]+'.txt')
    find.append(i)
    if(len(rows[i][0])!=15):
        #print(rows[i][0])
        
        txt.append(rows[i][0]+'.txt')
        arr=rows[i][5].split('-')
        string=rows[i][0]
        nstr="t"
        for i in arr:
            nstr+=i
        nstr+=string[1:]
        uqid.append(nstr)
        nstr+='.txt'
        file.append(nstr)
        #print(nstr)
    else:
        uqid.append(rows[i][0])

print(len(uqid),len(file))


# Get the list of all files and directories
path = "all_text"
dir_list = os.listdir(path)
cnt=0
check=[]
s=set()
for i in range(0,len(dir_list)):
  #print(len(i))
  
  if(len(dir_list[i])!=19):
      cnt+=1
      check.append(i)
      newpath=""
      newpath=path+'/'+dir_list[i]
      for idx in range(0,len(nl)):
          if(nl[idx]==dir_list[i]):
              #print(find[idx]+1,dir_list[i],uqid[idx])
              with open(newpath,'r', encoding="utf8") as f:
                  #print(f.read())
                  with open('extract/'+uqid[idx]+'.txt','w', encoding="utf8") as fl:
                      fl.write(f.read())
              f.close()
  #break  


print(len(nl),len(dir_list),'start building file')


with open('organizer_sample.csv', 'a',encoding="utf8") as f_object:
  
    # Pass this file object to csv.writer()
    # and get a writer object
            writer_object = writer(f_object)
  
    # Pass the list as an argument into
            List=["UNIQUE ID","SOURCE URL","SOURCE URL DATE","SOURCE URL TIME","CORRESPONDING URL","CORRESPONDING URL DATE","CORRESPONDING URL TIME","CORRESPONDING URL TITLE"]
    # the writerow()
            writer_object.writerow(List)
  
    #Close the file object
            f_object.close()



spl_idx=0
for idx in range(0,len(rows)-1):
        with open('organizer_sample.csv', 'a',encoding="utf8") as f_object:
  
    # Pass this file object to csv.writer()
    # and get a writer object
            #print('file write',idx+1)
            writer_object = writer(f_object)
  
    # Pass the list as an argument into
            List=[uqid[idx],rows[idx+1][1],rows[idx+1][2],rows[idx+1][3],rows[idx+1][4],rows[idx+1][5],rows[idx+1][6],rows[idx+1][7]]
    # the writerow()
            writer_object.writerow(List)
            #print("date",src_url_date[index])
  
    #Close the file object
            f_object.close()
        spl_idx+=1

print("process complete")






      
        
