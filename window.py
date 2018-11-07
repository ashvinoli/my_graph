import gi
gi.require_version('Gtk','3.0') #insure that the gtk version is 3
from gi.repository import Gtk
from graph import fig, check_and_plot
from matplotlib.backends.backend_gtk3agg import (FigureCanvasGTK3Agg as FigureCanvas)
counter=0
status = False #this variable keeps track of whether to plot on same or different plots. If true it is on same, else on different
function_list = [] #list to hold all the functions that have been requested for plot

def func_toggle(widget):
	global fig, counter #must code
	fig.clf()
	counter = 0
	for i in function_list:
		clicked("",i)
	

def reset_func(widget):
	global counter, function_list
	function_list = []
	fig.clf()
	counter = 0
	win.queue_draw()

def clicked(widget,function = ""): #remember that any callback function take the widget calling as their parameter
	global counter, status, btn_same, btn_diff,function_list

	if widget != "":
		function_list.append(func_input.get_text())

	string = ""
	if btn_diff.get_active() == True:
		status = True
	elif btn_same.get_active() == True:
		status = False


	if status == False:
		string = "s"
		counter=1
	else:
		string = "d"
		counter += 1
	if widget !="":
		check_and_plot(str(func_input.get_text()),counter,string)
	else:
		check_and_plot(function,counter,string)
	win.queue_draw() #This shit redraws the window. To redraw any widget just replace the win withe the widget
	#print(func_input.get_text())
	#print(function_list)

#main window
win = Gtk.Window()
win.connect("delete-event",Gtk.main_quit)
#win.set_default_size(800,600)
win.set_title("My very first GUI graph")


#Three boxes. One main Vertical will contain the horizontal ones. Two horizontal and a canvas will be vertically placed on the vertical box
v_box_horiz = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 2)
v_box_horiz_2 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 2)
v_box_horiz_3 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 2)
v_box_vert = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing = 0)
v_box_vert.pack_start(v_box_horiz,True,True,0)
v_box_vert.pack_start(v_box_horiz_2,True,True,0)

#Function input box that will be included in the horizontal v_box
func_input = Gtk.Entry()
v_box_horiz.pack_start(func_input,True,True,0)

#Error display and oli rocks label
my_label = Gtk.Label()
my_label.set_label("No copyright. Do whatever with this shit because OPENSOURCE and ASHVIN ROCK!")
v_box_horiz_3.pack_end(my_label,False,False,0)

#Plot Button
plot = Gtk.Button()
plot.set_label("Plot")
plot.connect("clicked",clicked)
v_box_horiz.pack_start(plot,True,True,0)

#clear button
reset = Gtk.Button()
reset.set_label("Clear")
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
canvas.set_size_request(700,500)
v_box_vert.pack_start(canvas,True,True,0)
#sw.add_with_viewport(canvas)
#sw.set_border_width(20)

#add vbox3 at the end
v_box_vert.pack_start(v_box_horiz_3,True,True,0)


#managing properties of main window and adding widgets that have been defined above
win.add(v_box_vert)


#check_and_plot("sin(x)",1,"s") #this function fills up the "fig" imported from other graph


win.show_all()
Gtk.main()



