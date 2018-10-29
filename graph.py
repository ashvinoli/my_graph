from extraction import evaluate_exp as e_exp
import numpy as np
import matplotlib.pyplot as plt
import math

#print(e_exp(a,1,2,3))


def eval_arr(x_arr,function):
	output = np.array([])
	for i in x_arr:
		output = np.append(output,e_exp(function,i))
	return output


def plot_function(function,begin=0,end=2*math.pi,interval=100):
	x = np.linspace(begin,end,interval)
	y = eval_arr(x,function)
	plt.plot(x,y)
	plt.show()

function = input("input function:")
plot_function(function)
