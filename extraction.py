import re

def extract(raw_string):
	pattern = r"[0-9]"
	try:
		new_strings = raw_string.split('=')
		new_strings = new_strings[1].split()
	except:
		new_strings = raw_string.split()
	
	tokens = []
	nums = ""
	for j in new_strings:
		for i in j:
			if re.match(pattern,i) or i == ".":
				nums = nums + i
			else:
				if nums != "":
					tokens.append(nums)
					nums = ""
				tokens.append(i)
		
	return tokens



text = input("PLACE:")
tokens = extract(text)
print(tokens)
