from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import nltk
import os.path
import multiprocessing
nltk.download('punkt')

directory=r'C:\Users\anand_zas2udg\Documents\Doc2Vec\beta1_2_essential_f\Groupby result\experiment'
docLabels=[]
docLabels=[f for f in os.listdir(directory)]
# print (docLabels)
data=[]
for doc in docLabels:
	words=open(directory+'\\'+ doc, encoding='utf-8').read()
	words=words.strip()
	words=words.split()
	# print (words)
	tags = [doc]
	data.append(TaggedDocument(words=words, tags=tags))
# print (data[0])

# encoding='cp1252'
# tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(data)]

cores=multiprocessing.cpu_count()
print (cores)
max_epochs = 20
vec_size = 250
alpha = 0.025

model = Doc2Vec(vector_size=vec_size,
				workers=cores,
                alpha=alpha, 
                min_alpha=0.00025,
                min_count=1,
                dm =1)
  
model.build_vocab(data)
# train_documents,total_examples=len(train_documents), epochs=30

model.train(data,total_examples=model.corpus_count,epochs=max_epochs)
                # =model.iter)
    # # decrease the learning rate
    # model.alpha -= 0.0002
    # # fix the learning rate, no decay
    # model.min_alpha = model.alpha
model.save("d2v.model")
print("Model Saved")