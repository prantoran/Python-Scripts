#tutorial source: Data School 
#link: https://www.youtube.com/watch?v=C56HbSJztT4
st = ['call you tonight','call me a cab','please call me..PLEASE']

#general steps of skikitlearn tools
#import, instantiate and fit a model
#CountVectorizer is not a model
#but it has the same APIs
#token = feature = word

#import and instantiate CountVectorizer (with the default parameters)
from sklearn.feature_extraction.text import CountVectorizer
v = CountVectorizer()

#learn the 'vocabulary' of the training data (occurs in-place)
v.fit(st)
print(v.fit(st))

#examine the fitted vocabulary
#Vectorizer returns unicode and sorted in alphabetical order
#no punctuations, ignores case
#it did not remove a because it was a stop word
#a is dropped because the default token_pattern drops words that are not atleast two characters

v.get_feature_names()
print(v.get_feature_names())

#transform training data into a 'document-term matrix's
#transforms do different things depending on the type of objects you are working with
#a document is s string, possibly containing multiple lines that you are 
#giving scikitlearn as a unit
st_dtm = v.transform(st)
print("")
print(st_dtm)
#convert sparse matrix to a dense matrix
print(st_dtm.toarray())

#examine the vocabulary and document-term matrix together
#document-tern matrix is a feature matrix with a fixed number of columns
import pandas as pd
print(pd.DataFrame(st_dtm.toarray(),columns = v.get_feature_names()))
print(pd.DataFrame(st_dtm.toarray()))
