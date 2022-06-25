import nltk
from nltk.tag.stanford import StanfordNERTagger
import pandas as pd
from helper import map_parallel
from os import getcwd, environ
from tqdm import tqdm

def tag(sentence, tagger):
    tokens = nltk.word_tokenize(sentence)
    tagged = tagger.tag(tokens)
    return tagged

java_bin = "C:/Program Files/Java/jdk-16.0.2/bin/java.exe"
environ["JAVAHOME"] = java_bin

tagger = StanfordNERTagger(
        f"./stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz",
        f"./stanford-ner/stanford-ner.jar",
    )

if __name__ == '__main__':
    dataset_name = input("Enter dataset name: ")

    print("reading dataset")
    df = pd.read_feather(f"./feather/{dataset_name}/aggregate")

    print(df.head())

    texts = df["text"].map(nltk.word_tokenize)
    _id = df["id"]

    cwd = getcwd()

    print("performing NER")

    output = map_parallel(
        tagger.tag, 
        texts,
        workers=5
    )

    print("NER complete")
    print("generating dataframe")

    df = pd.DataFrame(columns=["id", "entity", "label"])

    for i, o in tqdm(zip(_id, output)):
        # remove all occurrences of 'O'
        o = [x for x in o if x[1] != "O"]

        id_list = [i] * len(o)
        entity_list = [e[0] for e in o]
        label_list = [e[1] for e in o]

    
        df = df.append(
            pd.DataFrame({"id": id_list, "entity": entity_list, "label": label_list})
        )

    df.to_csv(f"./processed/ner-{dataset_name}.csv", index=False)