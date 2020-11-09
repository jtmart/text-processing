from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

model= Doc2Vec.load("d2v.model")
#to find the vector of a document which is not in training data
# test_data = word_tokenize("Six days ago, my colleagues and I sat on the chairs of high office in the Government of India.".lower())
test_data=open('abv_spe.txt', encoding='utf-8').read()
test_data=test_data.strip()
test_data=test_data.split()
test_data=list(test_data)
v1 = model.infer_vector(test_data)
print("V1_infer", v1)

# to find most similar doc using tags
similar_doc = model.docvecs.most_similar([v1])
print(similar_doc)

# model.docvecs.most_similar([vector]) 
# to find vector of doc in training data using tags or in other words, printing the vector of document at index 1 in training data
# print(model.docvecs)
	