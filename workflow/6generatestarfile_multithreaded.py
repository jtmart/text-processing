#-*- coding: utf-8 -*-
import csv
import multiprocessing

def script(thread_name, thread_limit, thread_number, totalfiles, reader):
    print(thread_name + "starting")
    
    string=' '
    latin_arr=[]
    simp=0
    target = 1 + thread_number #remove '1 + ' if the first row of the reader is not the names of the columns
    while target < totalfiles.value:
        temp_counter = 0
        row = ""
        for temp in reader:
            if temp_counter == target:
                row = temp
                break
            temp_counter += 1
        temp='**** '
        columns=len(row)
        
        for i in range (0,columns):
            if(row[i]==' ' or row[i]==''):
                row[i]='x'
            temp=temp+'*var{}_'.format(i+1)+str(row[i])+' '

        try:
            fi = open('all/{}.txt'.format(row[0]), 'rb')
            string=string+temp+'\n'+fi.read().decode("utf-8") +'\n'
            fi.close()

        except:
            print (thread_name + "latin")
            simp+=1
            latin_arr.append((row[0]))
            string=string+temp+'\n'+fi.read().decode("latin-1") +'\n'

        totalfiles.value -= 1
        print(thread_name, "files left ", totalfiles.value)
        target += thread_limit

    f.close()
        
    f=open('concat2.txt','w', encoding="utf-8")
    f.write(string)
    f.close()
    print (thread_name + simp)

    f2=open('latin_files_names.txt','w', encoding="utf-8")
    f2.write(latin_arr)
    f2.close()
    print(thread_name + latin_arr)


if __name__ == '__main__':
    t_limit = int(input("how many threads do you want? \n"))
    processes = []
    filename = r"metadata.csv"
    with open(filename,'r',encoding='utf-8') as f:
        reader_main = csv.reader(f)
        counter = -1
        for row in reader_main:
            counter += 1
        
        number_of_files = multiprocessing.Value("i", counter)
        for i in range(0,t_limit):
            name = "PROCESS " + str(i + 1) + ": "
            p = multiprocessing.Process(target=script, args=(name, t_limit, i, number_of_files, reader_main))
            p.start()
            processes.append(p)
        del [number_of_files, reader_main, counter]
        f.close()
    
    for process in processes:
        process.join()
        print(type())

    print("all processes finished")