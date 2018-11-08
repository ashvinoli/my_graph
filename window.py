import gi
gi.require_version('Gtk','3.0') #insure that the gtk version is 3
from gi.repository import Gtk, Gdk
from graph import fig, check_and_plot, check_and_plot_3d
from graph import err_log
from extraction import core_error
from matplotlib.backends.backend_gtk3agg import (FigureCanvasGTK3Agg as FigureCanvas)
import math

#Global Variables' declaration
counter=0
status = False #this variable keeps track of whether to plot on same or different plots. If true it is on same, else on different
function_list = [] #list to hold all the functions that have been requested for plot

def func_toggle(widget):
	global fig, counter, scale,scale_range #must code
	step_value = scale.get_value()
	range_value = scale_range.get_value()
	step_value = 1/step_value
	fig.clf()
	counter = 0
	for i in function_list:
		clicked("",i,range_value,step_value)
	

def reset_func(widget):
	global counter, function_list,scale,scale_range,my_label
	my_label.override_color(Gtk.StateFlags.NORMAL,Gdk.RGBA(0,0,1,1))
	my_label.set_label("----RESET-----")
	scale.set_value(5)
	scale_range.set_value(2*math.pi)
	function_list = []
	err_log.clear()
	core_error.clear()
	fig.clf()
	counter = 0
	win.queue_draw()

def clicked_namesake(widget):
	clicked("",func_input.get_text().lower(),is3d = True)	


def clicked(widget,function = "",range_value = 2*math.pi,step_value=0.02,is3d = False): #remember that any callback function take the widget calling as their parameter
	global counter, status, btn_same, btn_diff,function_list,my_label,scale,scale_range
	step_value = scale.get_value()
	range_value = scale_range.get_value()
	step_value = 1/step_value

	if is3d == False:
		if widget != "":
			function_list.append(func_input.get_text().lower())


	
		if btn_diff.get_active() == True:
			status = True
		elif btn_same.get_active() == True:
			status = False


		string = ""
		if status == False:
			string = "s"
			counter=1
		else:
			string = "d"
			counter += 1

		if widget !="":
			check_and_plot(str(func_input.get_text().lower()),counter,string,-1*range_value,range_value,step_value)
		else:
			check_and_plot(function,counter,string,-1*range_value,range_value,step = step_value)
	else:
		check_and_plot_3d(function,-1*range_value,range_value,step_value)

	if len(err_log) > 0 or len(core_error)>0:
		my_label.override_color(Gtk.StateFlags.NORMAL,Gdk.RGBA(1,0,0,1))
		err_message = ""
		for i in err_log:
			err_message = err_message + " " + i
		if len(core_error) > 0:
			my_label.set_label(core_error[len(core_error)-1] +"  "+err_message)
		else:
			my_label.set_label(err_message)
	else:
		my_label.override_color(Gtk.StateFlags.NORMAL,Gdk.RGBA(0,1,0,1))
		my_label.set_label("No Errors. Function Successfully Plotted!")
		
	win.queue_draw() #This shit redraws the window. To redraw any widget just replace the win withe the widget
	err_log.clear()
	core_error.clear()
	#print(func_input.get_text())
	#print(function_list)

#main window
win = Gtk.Window()
win.connect("delete-event",Gtk.main_quit)
#win.set_default_size(800,600)
win.set_title("Graph A")
win.set_position(Gtk.WindowPosition.CENTER)


#Three boxes. One main Vertical will contain the horizontal ones. Two horizontal and a canvas and the final horiz will be vertically placed on the vertical box
v_box_horiz = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 2)
v_box_horiz_2 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 2)
v_box_horiz_3 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 2)
v_box_horiz_smoothness = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 2)
v_box_horiz_range = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 2)
v_box_vert = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing = 0)
v_box_vert.pack_start(v_box_horiz,True,True,0)
v_box_vert.pack_start(v_box_horiz_2,True,True,0)

#Function input box that will be included in the horizontal v_box
func_input = Gtk.Entry()
v_box_horiz.pack_start(func_input,True,True,0)

#Error display and oli rocks label or just LABELS
my_label = Gtk.Label()
my_label.override_color(Gtk.StateFlags.NORMAL,Gdk.RGBA(0.3,0.5,0.7,1))
sens_label = Gtk.Label()
sens_label.set_label("Sampling rate/unit x:")
range_label = Gtk.Label()
range_label.set_label("Range (-value to + value):")
v_box_horiz_range.pack_start(range_label,False,False,0)
v_box_horiz_smoothness.pack_start(sens_label,False,False,0)
my_label.set_label("No copyright. Do whatever with this shit because OPENSOURCE and ASHVIN ROCK!")
v_box_horiz_3.pack_end(my_label,False,False,0)

#Plot Button
plot = Gtk.Button()
plot_3d = Gtk.Button()
plot.set_label("Plot")
plot_3d.set_label("3D-Plot")
plot.connect("clicked",clicked)
plot_3d.connect("clicked",clicked_namesake)
v_box_horiz.pack_start(plot,True,True,0)
v_box_horiz.pack_start(plot_3d,True,True,0)

#clear button
reset = Gtk.Button()
reset.set_label("Reset")
reset.connect("clicked",reset_func)
v_box_horiz.pack_start(reset,True,True,0)


#radio buttons to set the value of whther to plot on same graph or multiple graphs. Status variable will be updated
btn_same = Gtk.RadioButton.new_with_label_from_widget(None,"Same") #I really don't don what that new... does
#print(dir(btn_same.props))
btn_same.set_label("Plot on Same Graph")
btn_diff = Gtk.RadioButton.new_from_widget(btn_same) #Doing this places btn_diff on the same group as btn_same. That way only one radio button can be active at a time.....
btn_diff.set_label("Plot on Different Graphs")
btn_same.get_active()
#button connects
btn_same.connect("toggled",func_toggle)
btn_diff.connect("toggled",func_toggle)
#insert these buttons in the v_box_horiz_2
v_box_horiz_2.pack_start(btn_same,True,True,0)
v_box_horiz_2.pack_start(btn_diff,True,True,0)

#Scrolled window but i didn't put scrolled window instead I simply used canvas
sw = Gtk.ScrolledWindow()
#v_box_vert.pack_start(sw,True,True,0)
canvas = FigureCanvas(fig)
canvas.set_size_request(900,500)
v_box_vert.pack_start(canvas,True,True,0)
#sw.add_with_viewport(canvas)
#sw.set_border_width(20)



#Add scale to take sensitivity and range as input
ad1 = Gtk.Adjustment(10,1,100,1,50,0)
ad2 = Gtk.Adjustment(2*math.pi,0,100,1,1,0)
scale = Gtk.Scale(orientation = Gtk.Orientation.HORIZONTAL,adjustment = ad1)
scale.set_value(5)
scale_range = Gtk.Scale(orientation = Gtk.Orientation.HORIZONTAL,adjustment = ad2)
scale_range.connect("value-changed",func_toggle)
scale_range.set_value(2*math.pi)
scale.connect("value-changed",func_toggle)
#scale.set_label("Sensitivity")
v_box_horiz_range.pack_start(scale_range,True,True,0)
v_box_horiz_smoothness.pack_start(scale,True,True,0)

#add vbox3 and b_3 at the end after canvas
v_box_vert.pack_start(v_box_horiz_smoothness,True,True,0)
v_box_vert.pack_start(v_box_horiz_range,True,True,0)
v_box_vert.pack_start(v_box_horiz_3,True,True,0)


#managing properties of main window and adding widgets that have been defined above
win.add(v_box_vert)


#check_and_plot("sin(x)",1,"s") #this function fills up the "fig" imported from other graph


win.show_all()
Gtk.main()



