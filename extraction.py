import re
from collections import deque
import math


#global declaration of patterns
pattern_num = r"[0-9]+\.?[0-9]*"
pattern_signs = r"[\+,\-,\*,%,\^,/,\(,\)]"
pattern_signs_no_brackets = r"[\+,\-,\*,%,\^,/]"
#pattern_trig = r"[s,c,t,l,a][a-z]*\(.*\)" this shit matches everything between ( and ) ie sin(x) - cos(x) is also matched because of the parenthesis at the ends which i have coloned
pattern_trig = r"[s,c,t,l,a][a-z]*\(.*?\)" # this shit only matches sin(x)
pattern_alpha = r"[a-z]"
pattern_trig_raw = r"[s,c,t,l,a][a-z]*\([0-9]+\.?[0-9]*?\)"
pattern_trig_cos = r"cos\([0-9]+\.?[0-9]*?\)"
pattern_trig_sin = r"sin\([0-9]+\.?[0-9]*?\)"
pattern_trig_tan = r"tan\([0-9]+\.?[0-9]*?\)"
pattern_trig_log = r"log\([0-9]+\.?[0-9]*?\)"
pattern_trig_ln = r"ln\([0-9]+\.?[0-9]*?\)"
pattern_trig_arcsin = r"arcsin\([0-9]+\.?[0-9]*?\)"
pattern_trig_arccos = r"arccos\([0-9]+\.?[0-9]*?\)"
pattern_trig_arctan = r"arctan\([0-9]+\.?[0-9]*?\)"
pattern_trig_arcsinh = r"arcsinh\([0-9]+\.?[0-9]*?\)"
pattern_trig_arccosh = r"arccosh\([0-9]+\.?[0-9]*?\)"
pattern_trig_arctanh = r"arctanh\([0-9]+\.?[0-9]*?\)"



def evaluate_exp(raw_string,x=0.0,y=0.0,z=0.0):
	tokens = extract(raw_string)
	rpn = to_rpn(tokens)
	output = evaluate(rpn,x,y,z)
	return output


def evaluate(queue,x=0.0,y=0.0,z=0.0):
	output_queue = deque([])
	for i in queue:
		#print(i)
		if re.match(pattern_num,i):
			output_queue.append(float(i))
		elif re.match(pattern_trig_raw,i):
			if re.match(pattern_trig_sin,i):
				number = float(re.findall(pattern_num,i)[0])
				output_queue.append(math.sin(number))
			elif re.match(pattern_trig_cos,i):
				number = float(re.findall(pattern_num,i)[0])
				output_queue.append(math.cos(number))			
			elif re.match(pattern_trig_tan,i):
				number = float(re.findall(pattern_num,i)[0])
				output_queue.append(math.tan(number))	
			elif re.match(pattern_trig_log,i):
				try:
					number = float(re.findall(pattern_num,i)[0])
					output_queue.append(math.log10(number))	
				except:
					print("Error. Did you try to find log of 0 or negative numbers?")
					return -1
			elif re.match(pattern_trig_ln,i):
				try:
					number = float(re.findall(pattern_num,i)[0])
					output_queue.append(math.log(number))	
				except:
					print("Error. Did you try to find ln of 0 or negative numbers?")
					return -1
			elif re.match(pattern_trig_arcsin,i):
				try:
					number = float(re.findall(pattern_num,i)[0])
					output_queue.append(math.asin(number))	
				except:
					print("Arcsin's input out of range (-1,1)")
					return -1
			elif re.match(pattern_trig_arccos,i):
				number = float(re.findall(pattern_num,i)[0])
				output_queue.append(math.acos(number))	
			elif re.match(pattern_trig_arctan,i):
				number = float(re.findall(pattern_num,i)[0])
				output_queue.append(math.atan(number))	
			elif re.match(pattern_trig_arcsinh,i):
				number = float(re.findall(pattern_num,i)[0])
				output_queue.append(math.asinh(number))	
			elif re.match(pattern_trig_acosh,i):
				number = float(re.findall(pattern_num,i)[0])
				output_queue.append(math.acosh(number))	
			elif re.match(pattern_trig_atanh,i):
				number = float(re.findall(pattern_num,i)[0])
				output_queue.append(math.atanh(number))	
		
		elif re.match(pattern_trig,i):
			#print("reached")
			if i=="sin(x)":
				output_queue.append(math.sin(x))
			elif i=="cos(x)":
				output_queue.append(math.cos(x))
			elif i=="tan(x)":
				output_queue.append(math.tan(x))
			elif i == "log(x)":
				try:
					output_queue.append(math.log10(x))
				except:
					print("Error. Did you try log of 0 or negative numbers?")
					return -1
			elif i =="ln(x)":
				output_queue.append(math.log(x))
			elif i == "arcsin(x)":
				output_queue.append(math.asin(x))
			elif i == "arccos(x)":
				output_queue.append(math.acos(x))
			elif i == "arctan(x)":
				output_queue.append(math.atan(x))
			elif i == "arcsinh(x)":
				output_queue.append(math.asinh(x))
			elif i == "arccosh(x)":
				output_queue.append(math.acosh(x))
			elif i == "arctanh(x)":
				output_queue.append(math.atanh(x))
			elif i=="sin(y)":
				output_queue.append(math.sin(y))
			elif i=="cos(y)":
				output_queue.append(math.cos(y))
			elif i=="tan(y)":
				output_queue.append(math.tan(y))
			elif i == "log(y)":
				output_queue.append(math.log10(y))
			elif i == "ln(y)":
				output_queue.append(math.log(y))
			elif i == "arcsin(y)":
				output_queue.append(math.asin(y))
			elif i == "arccos(y)":
				output_queue.append(math.acos(y))
			elif i == "arctan(y)":
				output_queue.append(math.atan(y))
			elif i == "arcsinh(y)":
				output_queue.append(math.asinh(y))
			elif i == "arccosh(y)":
				output_queue.append(math.acosh(y))
			elif i == "arctanh(y)":
				output_queue.append(math.atanh(y))
			elif i=="sin(z)":
				output_queue.append(math.sin(z))
			elif i=="cos(z)":
				output_queue.append(math.cos(z))
			elif i=="tan(z)":
				output_queue.append(math.tan(z))
			elif i == "log(z)":
				output_queue.append(math.log10(z))
			elif i == "ln(z)":
				output_queue.append(math.log(z))
			elif i == "arcsin(z)":
				output_queue.append(math.asin(z))
			elif i == "arccos(z)":
				output_queue.append(math.acos(z))
			elif i == "arctan(z)":
				output_queue.append(math.atan(z))
			elif i == "arcsinh(z)":
				output_queue.append(math.asinh(z))
			elif i == "arccosh(z)":
				output_queue.append(math.acosh(z))
			elif i == "arctanh(z)":
				output_queue.append(math.atanh(z))
		
		elif re.match(pattern_signs_no_brackets,i):
			second = output_queue.pop()
			first = output_queue.pop()
			if i == '+':
				output_queue.append(first+second)
			elif i=='-':
				output_queue.append(first-second)
			elif i=='*':
				output_queue.append(first*second)
			elif i=='/':
				try:
					output_queue.append(first/second)
				except:
					print("Error. Perhaps division by zero attempt")
					return -1
			elif i=='^':
				output_queue.append(first**second)
			elif i=='%':
				output_queue.append(first%second)

		elif re.match(pattern_alpha,i):
			if i == 'x':
				output_queue.append(x)
			elif i == 'y':
				output_queue.append(y)
			elif i == 'z':
				output_queue.append(z)
			elif i == 'e':
				output_queue.append(math.e)
		
			
	return output_queue[0]	
	

		
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





