import re

#more bla bla bla 
#bla bla change
pattern = r"[A-Z]."
word = "ryP Ham"
matches = re.findall(pattern,word)
print(matches)
