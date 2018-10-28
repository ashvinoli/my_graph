import re

pattern = r"[A-Z]."
word = "ryP Ham"
matches = re.findall(pattern,word)
print(matches)
