import numpy as np
import matplotlib.pyplot as plt
from graph import eval_arr
from matplotlib.figure import Figure
import math

fig_stat = plt.figure("Regression")

def plot_best_fit(data_x,data_y,function,name,step = 0.2):
	x = np.arange(np.amin(data_x)-10,np.amax(data_x)+10,step)
	y = eval_arr(x,function)
	sub_plot = fig_stat.add_subplot(111)
	sub_plot.plot(x,y,label = name)
	sub_plot.scatter(data_x,data_y,marker = 'o', color = 'red')	
	sub_plot.legend()
	sub_plot.grid()
	plt.show()

def fit_poly(data_x,data_y,order): #data_x and data_y are np arrays of one dimension.
	mat_x = np.zeros((order,order))
	output = np.zeros((order,1))
	alg_exp = ""
	sample = ""
	for i in range(order):
		for j in range(order):
			mat_x[i,j] = (data_x**(i+j)).sum(axis = 0)

	for i in range(order):
		output[i] = ((data_x**(i))*data_y).sum(axis=0)

	unknowns = (np.linalg.inv(mat_x)).dot(output)
	counter = 0
	value = unknowns[0,0]
	alg_exp = str(value)
	alg_exp_name = str(round(value,3))
	for i in range(1,len(unknowns)):
		counter +=1
		value = unknowns[i,0]
		value_name = round(unknowns[i,0],3)
		alg_exp = alg_exp + "+" + "("+str(value)+")" +"*x^" + str(counter)
		alg_exp_name = alg_exp_name + "+" + "("+str(value_name)+")" +"*x^" + str(counter) #I am doing this just to name the function to lower dp.
	
	alg_exp = "(" + alg_exp+ ")"	
	plot_best_fit(data_x,data_y,alg_exp,alg_exp_name)

def cmd_input():
	go_on = True
	counter = 1
	data_x = np.array([])
	data_y = np.array([])
	while go_on:
		x = float(input("X%d:" %counter))
		y = float(input("Y%d:"%counter))
		data_x = np.append(data_x,x)
		data_y = np.append(data_y,y)
		anymore = input("Anymore:")
		if anymore in ["y","Yes","Y",]:
			go_on = True
		else:
			go_on = False
	
	order = int(input("Fit in order:"))
	unknowns = fit_poly(data_x,data_y,order+1)
	print(unknowns)
cmd_input()
