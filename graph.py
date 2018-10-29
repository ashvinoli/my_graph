from extraction import evaluate_exp as e_exp
import numpy as np
import matplotlib.pyplot as plt

#print(e_exp(a,1,2,3))


def eval_arr(x_arr,function):
	output = np.array([])
	for i in x_arr:
		output = np.append(output,e_exp(function,i))
	return output

function = input("input function:")
x = np.linspace(0,2,100)
y = eval_arr(x,function)
plt.plot(x,y)
plt.show()
