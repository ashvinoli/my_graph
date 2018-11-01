from extraction import evaluate_exp as e_exp
import numpy as np
import matplotlib.pyplot as plt
import math
import re
import sys

pattern_trig_general = r"sin|cos|tan|log|ln|log|arcsin|arccos|arctan|arcsinh|arccosh|arctanh"
pattern_trig = r"[s,c,t,l,a][a-z]*\(.*?\)"
pattern_trig_extend = r"[s,c,t,l,a][a-z]*\(.*\)"

def eval_arr(x_arr,function):
	output = np.array([])
	#length = 0
	for i in x_arr:
		#length+=1
		#print(i,e_exp(function,i))
		output = np.append(output,e_exp(function,i))	
	return output


def plot_function(function,value = 1,status='d',begin=0,end=2*math.pi,interval=100):
	x = np.linspace(begin,end,interval)
	y = eval_arr(x,function)
	if status=='d':
		plt.subplot(2,2,value)
		plt.plot(x,y,label=function) #k signigies the color of line
		plt.title(function)	
		plt.grid(True)
	elif status == 's':
		plt.plot(x,y,label=function)
		plt.legend()
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
	cnt_parent = count_parent(string)
	if cnt_parent == -1:
		print("Unmatched Parenthesis!")
		return -1
	total_matched = trig_equal_parent(string)
	if total_matched==-1:
		print("Put parenthesis after every sin, cos, tan..... like sin(x) or sin(sin(x))....")
		return -1
	if string == "":
		print("Empty function")
		return -1
	return 0
		


def show_all():
	#plt.legend()
	plt.show()

def main_input():
	check = 1
	value = 1
	if (len(sys.argv) == 1):
		print("No arguments passes. Please pass 's' or 'd' as arguments")
		return -1

	status = sys.argv[1].lower()

	if not(status =='d' or status =='s'):
		print("Wrong arguments passed. Please pass 's' or 'd' as arguments")
		return -1
	
	while check:
		function = input("Function %d Please:"% (value))
		correct = syntax_check(function)
		if correct == -1:
			print("Function %d will not be plotted." % (value))
		else:
			plot_function(function,value,status)
			value += 1
		print("\n")
		resp = (input("Anymore function?:")).lower()
		print("\n")
		if resp == 'n' or resp == 'no':
			check = 0
	show_all()	
		
main_input()



