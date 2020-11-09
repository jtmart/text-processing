from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize
import nltk
import os
nltk.download('punkt')

model= Doc2Vec.load("d2v.model")
#to find the vector of a document which is not in training data
# test_data = word_tokenize("Six days ago, my colleagues and I sat on the chairs of high office in the Government of India.".lower())
directory=r'/home/jtmartelli/dat/groupedloc_rec/' # on windows: 'C:\Users\anand_zas2udg\Documents\Doc2Vec\beta1_2_essential_f\Groupby result\Exp'
docLabels=[]
docLabels=[f for f in os.listdir(directory)]
for doc in docLabels:
	test_data=open(directory+'//'+ doc, encoding='utf-8').read() #change direction slashes if on windows
	print (doc)
	test_data=test_data.strip()
	test_data=test_data.split()
	test_data=list(test_data)
	v1 = model.infer_vector(test_data)
	similar_doc = model.docvecs.most_similar([v1])
    #print(similar_doc[0], similar_doc[1])
	print(similar_doc[0:10]) #will print the 10 most similar per locutor

# model.docvecs.most_similar([vector]) 
# to find vector of doc in training data using tags or in other words, printing the vector of document at index 1 in training data
# print(model.docvecs)
	