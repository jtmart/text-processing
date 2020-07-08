import csv
import os
import argparse
from nltk.tokenize import sent_tokenize

parser = argparse.ArgumentParser(description='Process files')
parser.add_argument('--corpus', type=str, default='round_1_script/corpus')
parser.add_argument('--csv_file', type=str, default='round_1_script/metadata_1.csv')
parser.add_argument('--output_folder', type=str, default='round_2_script')
parser.add_argument('--output_corpus_folder', type=str, default='round_2_script/corpus')
args = parser.parse_args()

if(not os.path.exists(args.output_corpus_folder)):
    os.makedirs(args.output_corpus_folder)

for file in os.listdir(args.corpus):
    with open(args.corpus+'/'+file, 'r') as f:
        text=sent_tokenize(f.read())
        segment = ''
        count = 1
        if(len(text)==0):
            file_name=file.strip('.txt') + '%04d' % count + '.txt'
            with open(f'{args.output_corpus_folder}/{file_name}', "w") as outfile:
                outfile.write(segment)
        for i in range(len(text)):
            segment= segment + ' ' + text[i]
            if (len(segment) > 260 and i!=len(text)-2) or i==len(text)-1:
                file_name=file.strip('.txt') + '%04d' % count + '.txt'
                with open(f'{args.output_corpus_folder}/{file_name}', "w") as outfile:
                    outfile.write(segment)
                count+=1
                segment=''

with open(args.csv_file, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data_dict={}
data_csv=[]
for d in data:
    data_dict[d[0]]=d

print(data_dict.keys())
data_csv.append(data_dict["id"])

for file in sorted(os.listdir(args.output_corpus_folder)):
    entry=data_dict[file[:-8]].copy()
    entry[0]=file[:-4]
    entry[-1]=file[-8:-4]
    data_csv.append(entry)

with open(args.output_folder+'/metadata_2.csv', 'w') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, delimiter=',')
     for i in data_csv:
         wr.writerow(i)
