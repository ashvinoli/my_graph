from extraction import evaluate_exp as e_exp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import math
import re
import sys

pattern_trig_general = r"sin|cos|tan|log|ln|log|arcsin|arccos|arctan|arcsinh|arccosh|arctanh"
pattern_trig = r"[s,c,t,l,a][a-z]*\(.*?\)"
pattern_trig_extend = r"[s,c,t,l,a][a-z]*\(.*\)"
pattern_signs_no_brackets = r"[\+,\-,\*,%,\^,/]"
pattern_signs_end = r"[\+,\-,\*,%,\^,/]$"
fig  = Figure(figsize = (5,4),dpi=100)
err_log =[] #to report errors
def bracket_check(string):
	slight_tokens=[]
	while len(string) >0:
		if re.match(pattern_trig_general,string):
			matches = re.findall(pattern_trig_general,string)			
			slight_tokens.append(matches[0])
			string = string[len(matches[0]):]
		else:
			slight_tokens.append(string[:1])
			string = string[1:]

	for i in range(len(slight_tokens)-1):
		if re.match(pattern_trig_general,slight_tokens[i]):
			if not(re.match("\(",slight_tokens[i+1])):
				return -1

	

def sign_check(string):
	#print(string)
	if re.match(pattern_signs_end,string[len(string)-2]):
		return -1
	for i in range((len(string)-1)):
		if re.match(pattern_signs_no_brackets,string[i]) and re.match(pattern_signs_no_brackets,string[i+1]):
			return -1 	


def eval_arr(x_arr,function):
	output = np.array([])
	#length = 0
	for i in x_arr:
		#length+=1
		#print(i,e_exp(function,i))
		output = np.append(output,e_exp(function,i))	
	return output


def plot_function(function,value = 1,status='d',begin=-2*math.pi,end=2*math.pi,step = 0.2):
	global fig
	x = np.arange(begin,end,step)
	y = eval_arr(x,function)
	if status=='d':
		a = fig.add_subplot(2,2,value)
		#plt.subplot(2,2,value)
		a.plot(x,y,label=function) #k signigies the color of line
		a.set_title(function)	
		a.grid(True)
	elif status == 's':
		a = fig.add_subplot(111)
		a.plot(x,y,label=function)
		a.legend()		
		a.grid(True)
	else:
		print("Wrong status argument.")
	#plt.xlabel('x')
	#plt.ylabel('y')
	#plt.xscale('linear')
	#plt.yscale('log')

def count_parent(string):
	total = 0
	for i in string:
		if i=="(":
			total +=1;
		elif i==")":
			total -=1;
	if total!=0:
		return -1
	else:
		return 0

def trig_equal_parent(string):
	total_trigs = len(re.findall(pattern_trig_general,string))
	total_brackets = 0
	for i in string:
		if i=="(" or i==")":
			total_brackets +=1;
		
	if total_brackets >= 2*total_trigs:
		return 0
	else:
		return -1

	
	
def syntax_check(string):
	if string == "()":
		err_log.append("Empty function")
		return -1

	sign_error = sign_check(string)
	if sign_error == -1:
		err_log.append("Syntax error.Check the operators.")
		return -1
	
	bracket = bracket_check(string)
	if bracket == -1:
		err_log.append("Trig Syntax Error.")
		return -1

	cnt_parent = count_parent(string)
	if cnt_parent == -1:
		err_log.append("Unmatched Parenthesis!")
		return -1

	total_matched = trig_equal_parent(string)
	if total_matched==-1:
		err_log.append("Put parenthesis after every sin, cos, tan..... like sin(x) or sin(sin(x))....")
		return -1
	
	return 0
		


def show_all():
	global fig
	#plt.legend()
	fig.show()


def add_brackets(string):
	string = "("+string+")"
	return string

def main_input():
	check = 1
	value = 1
	if (len(sys.argv) == 1):
		print("No arguments passed. Please pass 's' or 'd' as arguments.")
		return -1

	status = sys.argv[1].lower()

	if not(status =='d' or status =='s'):
		print("Wrong arguments passed. Please pass 's' or 'd' as arguments.")
		return -1
	
	while check:
		function = input("Function %d Please:"% (value))
		#print(function)
		function = add_brackets(function)
		#print(function)
		correct = syntax_check(function)
		if correct == -1:
			err_log.append("Function %d will not be plotted." % (value))
		else:
			plot_function(function,value,status)
			value += 1
		print("\n")
		resp = (input("Anymore function?:")).lower()
		print("\n")
		if resp == 'n' or resp == 'no':
			check = 0
	show_all()	

def check_and_plot(function,value,status="s",range_x_init=-2*math.pi,range_x_final = 2*math.pi,step=0.2):
	function = add_brackets(function)
	correct = syntax_check(function)
	if correct == -1:
		err_log.append("Function will not be plotted")
	else:
		plot_function(function, value, status,range_x_init,range_x_final,step)
			
#main_input()




