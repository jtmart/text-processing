import os
import glob
import pandas as pd
os.chdir("/home/ubuntu/MyNotebooks/v3/src/_temp/outputs/")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f, header = 0, lineterminator='\n', sep=',', error_bad_lines=False, index_col=False, dtype='unicode') for f in all_filenames])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

#import glob
#import csv
#interesting_files = glob.glob("/home/ubuntu/MyNotebooks/v3/src/_temp/outputs/*.csv") 

#header_saved = False
#with open('/home/tcs/PYTHONMAP/output.csv', 'w') as fout:
    #writer = csv.writer(fout)
    #for filename in interesting_files:
        #with open(filename) as fin:
            #header =  next(fin)
            #if not header_saved:
                #writer.writerows(header) # you may need to work here. The writerows require an iterable.
                #header_saved = True
            #writer.writerows(fin.readlines())