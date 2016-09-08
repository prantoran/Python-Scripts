#metacharacters
#/. matches any character
#/w matches any word character [a-zA-Zs0-9_]
#/W matches non-word character [^a-zA-Z0-9_]
#/w/w matches a word with 2 word characters
#/d matches any digit
#/d.. matches a digit and two characters after that
#/w.. matches a word charactera and ,,
#left to right
#\s whitespace character
#\s+ 1 or more spaces
#\S non-whitespace character

import re

def Find(pat,text):
    match = re.search(pat,text) #returns a match object
    #print(match)
    #print(match.group())
    if match: print(match.group())
    else: print("not found")
    
Find('ate','I ate cookies')
Find('.e','I ate cookies')
Find('1\.L','1.Lalaland')
Find(r'1\.L','1.Lalaland') #r indicates to not do any special processing with backlashes
Find(r':\w\w\w','blah :cat blah blah')
Find(r'\d\d\d','blah blah 12312 blah 999999')
Find(r'\d\d\s\w','blah blah 12312 blah 999999')

Find(r'\d\d\s\w','blah blah 12312                            blah 999999 blah')

Find(r'\d\d\s+\w','blah blah 12312                            blah 999999 blah')
Find(r':\w+','blah blah :kitten blah blah')
Find(r':.+','blah blah :kitten blah blah')
Find(r'\w+@\w+\.\w+','blah nick.p@gmail.com yatta @ ')
Find('[\w.]+@\w+','blah nick.p@gmail.com yatta @ ') #[\w.] defines the set of characters to consider
Find('[\w.]+@[\w.]+','blah nick.p@gmail.com yatta @ ')


m = re.search(r'([\w.]+)@([\w.]+)','blah nick.p@gmail.com yatta @ ') #() creates seperate groups that can be accessed seperately using indexes
print(m.group())
print(m.group(1))
print(m.group(2))

n = re.findall(r'[\w.]+@[\w.]+','blah nick.p@gmail.com yatta foo@bar ')
print(n)

nn =re.findall(r'([\w.]+)@([\w.]+)','blah nick.p@gmail.com yatta foo@bar Foool@bo')
print(nn)
print(dir(re))

nnn =re.findall(r'([\w.]+)@([\w.]+)','blah nick.p@gmail.com yatta foo@bar Foool@bo',re.IGNORECASE)
print(nnn)
