import re
from collections import deque
import math


#global declaration of patterns
pattern_num = r"[0-9]+\.?[0-9]*"
pattern_negative_num = r"\-{0,1}[0-9]+\.?[0-9]*"
pattern_signs = r"[\+,\-,\*,%,\^,/,\(,\),#,@]"
pattern_signs_no_brackets = r"[\+,\-,\*,%,\^,/,#,@]"
pattern_trig_extend = r"[s,c,t,l,a][a-z]*\(.*\)" #this matches everything between ( and ) ie sin(x) - cos(x) is also matched because of the parenthesis at the ends which i have coloned
pattern_trig = r"[s,c,t,l,a][a-z]*\(.*?\)" # this only matches sin(x)
pattern_alpha = r"[a-z]"
pattern_trig_raw = r"[s,c,t,l,a][a-z]*\(\-{0,1}[0-9]+\.?[0-9]*?\)"
pattern_trig_cos = r"cos\(\-{0,1}[0-9]+\.?[0-9]*?\)"
pattern_trig_sin = r"sin\(\-{0,1}[0-9]+\.?[0-9]*?\)"
pattern_trig_tan = r"tan\(\-{0,1}[0-9]+\.?[0-9]*?\)"
pattern_trig_log = r"log\(\-{0,1}[0-9]+\.?[0-9]*?\)"
pattern_trig_ln = r"ln\(\-{0,1}[0-9]+\.?[0-9]*?\)"
pattern_trig_arcsin = r"arcsin\(\-{0,1}[0-9]+\.?[0-9]*?\)"
pattern_trig_arccos = r"arccos\(\-{0,1}[0-9]+\.?[0-9]*?\)"
pattern_trig_arctan = r"arctan\(\-{0,1}[0-9]+\.?[0-9]*?\)"
pattern_trig_arcsinh = r"arcsinh\(\-{0,1}[0-9]+\.?[0-9]*?\)"
pattern_trig_arccosh = r"arccosh\(\-{0,1}[0-9]+\.?[0-9]*?\)"
pattern_trig_arctanh = r"arctanh\(\-{0,1}[0-9]+\.?[0-9]*?\)"
pattern_trig_general = r"sin|cos|tan|log|ln|log|arcsin|arccos|arctan|arcsinh|arccosh|arctanh"



def evaluate_exp(raw_string,x=0.0,y=0.0,z=0.0):
	tokens = extract(raw_string)
	#print(tokens)
	rpn = to_rpn(tokens)
	#print(rpn)
	output = evaluate(rpn,x,y,z)
	#print(output)
	return output


def evaluate(queue,x=0.0,y=0.0,z=0.0):
	output_queue = deque([])
	for i in queue:
		#print(i)
		if re.match(pattern_num,i):
			output_queue.append(float(i))
		elif re.match(pattern_trig_raw,i):
			if re.match(pattern_trig_sin,i):
				number = float(re.findall(pattern_negative_num,i)[0])
				output_queue.append(round((math.sin(number)),8))
			elif re.match(pattern_trig_cos,i):
				number = float(re.findall(pattern_negative_num,i)[0])
				output_queue.append(round((math.cos(number),8)))			
			elif re.match(pattern_trig_tan,i):
				number = float(re.findall(pattern_negative_num,i)[0])
				output_queue.append(round((math.tan(number)),8))	
			elif re.match(pattern_trig_log,i):
				try:
					number = float(re.findall(pattern_negative_num,i)[0])
					output_queue.append(round((math.log10(number)),8))	
				except:
					print("Error. Did you try to find log of 0 or negative numbers?")
					return -1
			elif re.match(pattern_trig_ln,i):
				try:
					number = float(re.findall(pattern_negative_num,i)[0])
					output_queue.append(round((math.log(number)),8))	
				except:
					print("Error. Did you try to find ln of 0 or negative numbers?")
					return -1
			elif re.match(pattern_trig_arcsin,i):
				try:
					number = float(re.findall(pattern_negative_num,i)[0])
					output_queue.append(round((math.asin(number)),8))	
				except:
					print("Arcsin's input out of range (-1,1)")
					return -1
			elif re.match(pattern_trig_arccos,i):
				number = float(re.findall(pattern_negative_num,i)[0])
				output_queue.append(round((math.acos(number)),8))	
			elif re.match(pattern_trig_arctan,i):
				number = float(re.findall(pattern_negative_num,i)[0])
				output_queue.append(round((math.atan(number)),8))	
			elif re.match(pattern_trig_arcsinh,i):
				number = float(re.findall(pattern_negative_num,i)[0])
				output_queue.append(round((math.asinh(number)),8))	
			elif re.match(pattern_trig_arccosh,i):
				number = float(re.findall(pattern_negative_num,i)[0])
				output_queue.append(round((math.acosh(number)),8))
			elif re.match(pattern_trig_arctanh,i):
				number = float(re.findall(pattern_negative_num,i)[0])
				output_queue.append(round((math.atanh(number)),8))	
		
		elif re.match(pattern_trig_extend,i):
			#print("reached")
			if i=="sin(x)":
				output_queue.append(round((math.sin(x)),8))
			elif i=="cos(x)":
				output_queue.append(round((math.cos(x)),8))
			elif i=="tan(x)":
				output_queue.append(round((math.tan(x)),8))
			elif i == "log(x)":
				try:
					output_queue.append(round((math.log10(x)),8))
				except:
					print("Error. Did you try log of 0 or negative numbers?")
					return -1
			elif i =="ln(x)":
				#output_queue.append(round((math.log(x)),8))
				try:
					output_queue.append(round((math.log(x)),8))
				except:
					print("Error. Did you try ln of 0 or negative numbers?")
					return -1
			elif i == "arcsin(x)":
				output_queue.append(round((math.asin(x)),8))
			elif i == "arccos(x)":
				output_queue.append(round((math.acos(x)),8))
			elif i == "arctan(x)":
				output_queue.append(round((math.atan(x)),8))
			elif i == "arcsinh(x)":
				output_queue.append(round((math.asinh(x)),8))
			elif i == "arccosh(x)":
				output_queue.append(round((math.acosh(x)),8))
			elif i == "arctanh(x)":
				output_queue.append(round((math.atanh(x)),8))
			elif i=="sin(y)":
				output_queue.append(round((math.sin(y)),8))
			elif i=="cos(y)":
				output_queue.append(round((math.cos(y)),8))
			elif i=="tan(y)":
				output_queue.append(round((math.tan(y)),8))
			elif i == "log(y)":
				output_queue.append(round((math.log10(y)),8))
			elif i == "ln(y)":
				output_queue.append(round((math.log(y)),8))
			elif i == "arcsin(y)":
				output_queue.append(round((math.asin(y)),8))
			elif i == "arccos(y)":
				output_queue.append(round((math.acos(y)),8))
			elif i == "arctan(y)":
				output_queue.append(round((math.atan(y)),8))
			elif i == "arcsinh(y)":
				output_queue.append(round((math.asinh(y)),8))
			elif i == "arccosh(y)":
				output_queue.append(round((math.acosh(y)),8))
			elif i == "arctanh(y)":
				output_queue.append(round((math.atanh(y)),8))
			elif i=="sin(z)":
				output_queue.append(round((math.sin(z)),8))
			elif i=="cos(z)":
				output_queue.append(round((math.cos(z)),8))
			elif i=="tan(z)":
				output_queue.append(round((math.tan(z)),8))
			elif i == "log(z)":
				output_queue.append(round((math.log10(z)),8))
			elif i == "ln(z)":
				output_queue.append(round((math.log(z)),8))
			elif i == "arcsin(z)":
				output_queue.append(round((math.asin(z)),8))
			elif i == "arccos(z)":
				output_queue.append(round((math.acos(z)),8))
			elif i == "arctan(z)":
				output_queue.append(round((math.atan(z)),8))
			elif i == "arcsinh(z)":
				output_queue.append(round((math.asinh(z)),8))
			elif i == "arccosh(z)":
				output_queue.append(round((math.acosh(z)),8))
			elif i == "arctanh(z)":
				output_queue.append(round((math.atanh(z)),8))
			else:
				re_token = extract(re.findall("\(.*\)",i)[0])
				#print(re_token)
				re_torpn = to_rpn(re_token)
				#print(re_torpn)
				re_value = evaluate(re_torpn,x,y,z)
				#print(re_value)
				#print(i)
				#final = evaluate(i[:len(i)-len(re_token)]+"(" + str(re_value) + ")",x,y,z)
				length = len(re.findall(pattern_trig_general,i)[0])	
				re_lst = [i[:length]+"(" + str(re_value) + ")"]
				#print(i,re_lst)
				final = evaluate(re_lst,x,y,z)
				#print(final)
				output_queue.append(final)
				
		
		elif re.match(pattern_signs_no_brackets,i):
			#signs = 0
			#not_signs = 0
			#unary_mode = False
			#for i in queue:
			#	if re.match(pattern_signs_no_brackets,i):
			#		signs +=1
			#	else:
			#		not_signs += 1
			#if signs >= not_signs:
			#	unary_mode = True			
						
			


			#second = output_queue.pop()
			#first = 0.0
			#if len(output_queue) != 0:
				#first = output_queue.pop()

			if i=='#':
				second = output_queue.pop()
				output_queue.append((-1)*second)
			elif i=='@':
				second = output_queue.pop()
				output_queue.append(second)
			elif i == '+':
				second = output_queue.pop()
				first = output_queue.pop()
				output_queue.append(first+second)
			elif i=='-':
				second = output_queue.pop()
				first = output_queue.pop()
				output_queue.append(first-second)
			elif i=='*':
				second = output_queue.pop()
				first = output_queue.pop()
				output_queue.append(first*second)
			elif i=='/':
				second = output_queue.pop()
				first = output_queue.pop()
				try:
					output_queue.append(first/second)
				except:
					print("Error. Perhaps division by zero attempt")
					return -1
			elif i=='^':
				second = output_queue.pop()
				first = output_queue.pop()
				output_queue.append(first**second)
			elif i=='%':
				second = output_queue.pop()
				first = output_queue.pop()
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
			else:
				print("Unknown Variable '%c' uncountered!" % (i))
				return -1
			
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
				#print(read_op)
				if not(read_op == ')' or read_op == '('):
					while comp_op(read_op,i):
						output_queue.append(op_stack.pop())
						if len(op_stack)!=0:
							read_op = op_stack[len(op_stack)-1]
							if read_op == ')' or read_op == '(':
								break
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
	op = {'+':0, '-':1, '*':2,'/':2,'%':2,'^':3,'#':1,'@':0}
	return op[first] >= op[second]

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
		elif re.match(pattern_trig_general,single_piece):
			word = re.findall(pattern_trig_general,single_piece)
			extra_piece = match_paren(single_piece[len(word[0]):])
			total_word = word[0] + extra_piece
			#print(word[0])
			#print(total_word)
			tokens.append(total_word)
			single_piece = single_piece[len(total_word):]
		elif re.match(pattern_alpha,single_piece):
			word = re.findall(pattern_alpha,single_piece)
			tokens.append(word[0])
			single_piece = single_piece[len(word[0]):]
	
	ast_list = ["*"]
	i=0
	while i < len(tokens)-1:
		if (re.match(pattern_num,tokens[i]) and (re.match(pattern_alpha,tokens[i+1]) or re.match(pattern_trig,tokens[i+1]) or re.match("\(",tokens[i+1]) )) or (re.match(pattern_trig,tokens[i]) and re.match(pattern_trig,tokens[i+1]) ):
			tokens = tokens[:i+1] + ast_list + tokens[i+1:]
		i = i+1 
	for i in range(len(tokens)-1):
		if re.match("\(",tokens[i]) and re.match("\-",tokens[i+1]):
			tokens[i+1] = '#'
		if re.match("\(",tokens[i]) and re.match("\+",tokens[i+1]):
			tokens[i+1] = '@'
	return tokens	



def match_paren(string):
	counter = 0
	extracted = ""
	for i in string:
		extracted = extracted + i
		if i=="(":
			counter+=1
		if i==")":
			counter -=1
		if counter==0:
			break
	
	if counter !=0:
		print("No matching prenthesis.")
		return -1			
	return extracted


