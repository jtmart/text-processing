import csv
import os
import argparse

parser = argparse.ArgumentParser(description='Process files')
parser.add_argument('--corpus', type=str, default='corpus')
parser.add_argument('--csv_file', type=str, default='metadata.csv')
parser.add_argument('--output_folder', type=str, default='round_1_script')
parser.add_argument('--output_corpus_folder', type=str, default='round_1_script/corpus')
args = parser.parse_args()

for file in os.listdir(args.corpus):
    with open(args.corpus+'/'+file, 'r', encoding='utf-8') as f:
        content=f.read().replace('\n','').split('****')[1:]
        file_name=file.strip('.txt')
        for c in content:
            if(not os.path.exists(args.output_corpus_folder)):
                os.makedirs(args.output_corpus_folder)
            with open(f'{args.output_corpus_folder}/{file_name+c[:3]}.txt', "w") as outfile:
                outfile.write(c[3:])

with open(args.csv_file, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data_dict={}
data_csv=[]
for d in data:
    print(d[0])
    data_dict[d[0]]=d

data_csv.append(data_dict["id"])

for file in sorted(os.listdir(args.output_corpus_folder)):
    entry=data_dict[file[:-7]].copy()
    entry[0]=file[:-4]
    entry[-2]=file[-7:-4]
    data_csv.append(entry)


with open(args.output_folder+'/metadata_1.csv', 'w') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, delimiter=',')
     for i in data_csv:
         wr.writerow(i)
