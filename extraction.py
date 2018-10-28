import re
from collections import deque

#global declaration of patterns
pattern_num = r"[0-9]+\.?[0-9]*"
pattern_signs = r"[\+,\-,\*,%,\^,/,\(,\)]"
pattern_signs_no_brackets = r"[\+,\-,\*,%,\^,/]"
#pattern_trig = r"[s,c,t,l,a][a-z]*\(.*\)" this shit matches everything between ( and ) ie sin(x) - cos(x) is also matched because of the parenthesis at the ends which i have coloned
pattern_trig = r"[s,c,t,l,a][a-z]*\(.*?\)" # this shit only matches sin(x)
pattern_alpha = r"[a-z]"


def to_rpn(tokens):
	output_queue = deque([])
	op_stack = []
	
	for i in tokens:
		if re.match(pattern_num,i) or re.match(pattern_alpha,i) or re.match(pattern_trig,i):
			output_queue.append(i)
		elif re.match(pattern_signs_no_brackets,i):
			if len(op_stack)==0:
				op_stack.append(i)
			
			else:
				read_op = op_stack[len(op_stack)-1]
				if not(read_op == ')' or read_op == '('):
					while comp_op(read_op,i):
						output_queue.append(op_stack.pop())
						if len(op_stack)!=0:
							read_op = op_stack[len(op_stack)-1]
						else:	
							break
				op_stack.append(i)
				
		elif i=='(':
			op_stack.append(i)
		elif i==')':
			read_op = op_stack[len(op_stack)-1]
			while read_op != '(':
				#print(op_stack)
				output_queue.append(op_stack.pop())
				read_op = op_stack[len(op_stack)-1]
			op_stack.pop()
		#print(op_stack)
	for i in range(len(op_stack)):	
		output_queue.append(op_stack.pop())	
	return output_queue				

def comp_op(first,second):
	op = {'+':0, '-':1, '*':2,'/':2,'%':2,'^':3}
	return op[first] > op[second]

def extract(raw_string):
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
	
	ast_list = ["*"]
	i=0
	while i < len(tokens)-1:
		if re.match(pattern_num,tokens[i]) and (re.match(pattern_alpha,tokens[i+1]) or re.match(pattern_trig,tokens[i+1]) ):
			tokens = tokens[:i+1] + ast_list + tokens[i+1:]
		i = i+1 
	return tokens	



text = input("PLACE:")
tokens = extract(text)
print(tokens)
print(to_rpn(tokens))
