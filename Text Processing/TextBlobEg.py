#reference: http://adhikary.net/post/getting-started-nlp-1/
from textblob import TextBlob

text = "Damm I forgot to wake up and missed the 9am class on Friday. I am going to regret it."
blob = TextBlob(text) #creating TextBlob object from text string
print(blob.sentences)
#sentences are 0 indexed
print(blob.sentences[0].words)

#Parts of Speech (PoS)
#individual words of a sentence, classified into categories such as nouns, verbs etc
for u in blob.sentences[0].pos_tags:
    print(u) #pos_tag of each word in sentence[0]

import nltk
print(nltk.help.upenn_tagset('NNP'))

lw = blob.sentences[1].words[0]
print(lw)
print(lw.pluralize()) #I -> We

marked_word = blob.sentences[1].words[2]
print(marked_word.get_synsets())



