import re

def extract(raw_string):
	pattern_num = r"[0-9]+\.?[0-9]*"
	pattern_signs = r"[\+,\-,\*,%,\^,/,\(,\)]"
	#pattern_trig = r"[s,c,t,l,a][a-z]*\(.*\)" this shit matches everything between ( and ) ie sin"("x) - cos(x")" is also matched because of the parenthesis at the ends which i have coloned
	pattern_trig = r"[s,c,t,l,a][a-z]*\(.*?\)" # this shit only matches sin(x)
	pattern_alpha = r"[a-z]"
	try:
		new_strings = raw_string.split('=')
		new_strings = new_strings[1].split()
	except:
		new_strings = raw_string.split()
	
	single_piece = ""
	tokens = []
	for i in new_strings:
		single_piece = single_piece + i;
	#print(single_piece)
	while len(single_piece) > 0:
		if re.match(pattern_num,single_piece):
			word = re.findall(pattern_num,single_piece)
			tokens.append(word[0])
			single_piece = single_piece[len(word[0]):]
		elif re.match(pattern_signs,single_piece):
			word = re.findall(pattern_signs,single_piece)
			tokens.append(word[0])
			single_piece = single_piece[len(word[0]):]
		elif re.match(pattern_trig,single_piece):
			word = re.findall(pattern_trig,single_piece)
			#print(word[0])
			tokens.append(word[0])
			single_piece = single_piece[len(word[0]):]
		elif re.match(pattern_alpha,single_piece):
			word = re.findall(pattern_alpha,single_piece)
			tokens.append(word[0])
			single_piece = single_piece[len(word[0]):]

	return tokens	

text = input("PLACE:")
tokens = extract(text)
print(tokens)
