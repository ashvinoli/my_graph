import numpy as np


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
	for i in range(1,len(unknowns)):
		counter +=1
		value = unknowns[i,0]
		alg_exp = alg_exp + "+" + str(value) +"*x^" + str(counter) 
	return alg_exp

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
		if anymore in ["y","Yes","Y"]:
			go_on = True
		else:
			go_on = False
	
	order = int(input("Fit in order:"))
	unknowns = fit_poly(data_x,data_y,order+1)
	print(unknowns)
cmd_input()
