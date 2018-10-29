from extraction import evaluate_exp as e_exp
import numpy as np
import matplotlib.pyplot as plt
import math
import re

pattern_trig_general = r"sin|cos|tan|log|ln|log|arcsin|arccos|arctan|arcsinh|arccosh|arctanh"
pattern_trig = r"[s,c,t,l,a][a-z]*\(.*?\)"
pattern_trig_extend = r"[s,c,t,l,a][a-z]*\(.*\)"

def eval_arr(x_arr,function):
	output = np.array([])
	for i in x_arr:
		print(i,e_exp(function,i))
		output = np.append(output,e_exp(function,i))
		
	return output


def plot_function(function,begin=0,end=2*math.pi,interval=100):
	x = np.linspace(begin,end,interval)
	y = eval_arr(x,function)
	plt.plot(x,y)
	plt.show()

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
		
	if total_brackets == 2*total_trigs:
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
	return 0
		

function = input("input function:")
valid = syntax_check(function)
#print(e_exp(function))
if valid==0:
	plot_function(function)
