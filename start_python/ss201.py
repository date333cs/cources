#!/usr/bin/python
import sys
 
dictionary = {}

f = open("king_james_bible_tokenized.txt")
 
data = f.read()
 
doc = data.split()
 
for k in doc:
        dictionary[k] = dictionary.get(k,0) + 1
 
list = sorted(dictionary.items(), key=lambda x:x[1], reverse=True)
 
for k, v in list[:30]:
    print (k, v)
