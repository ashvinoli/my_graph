import gi
gi.require_version('Gtk','3.0') #insure that the gtk version is 3
from gi.repository import Gtk
from graph import fig, check_and_plot
from matplotlib.backends.backend_gtk3agg import (FigureCanvasGTK3Agg as FigureCanvas)
counter=0

def reset_func(widget):
	fig.clf()
	win.queue_draw()

def clicked(widget): #remember that any callback function take the widget calling as their parameter
	#print(widget)
	global counter
	counter+=1
	check_and_plot(str(func_input.get_text()),counter,"s")
	win.queue_draw() #This shit redraws the window. To redraw any widget just replace the win withe the widget
	#print(func_input.get_text())

#main window
win = Gtk.Window()
win.connect("delete-event",Gtk.main_quit)
#win.set_default_size(800,600)
win.set_title("My very first GUI graph")


#Two boxes. Vertical will contain the horizontal.
v_box_horiz = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 2)
v_box_vert = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing = 0)
v_box_vert.pack_start(v_box_horiz,True,True,0)

#Function input box that will be included in the horizontal v_box
func_input = Gtk.Entry()
v_box_horiz.pack_start(func_input,True,True,0)

#Error display label


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

#Scrolled window
sw = Gtk.ScrolledWindow()
#v_box_vert.pack_start(sw,True,True,0)
canvas = FigureCanvas(fig)
canvas.set_size_request(600,500)
v_box_vert.pack_start(canvas,True,True,0)
#sw.add_with_viewport(canvas)
#sw.set_border_width(20)


#managing properties of main window and adding widgets that have been defined above
win.add(v_box_vert)


#check_and_plot("sin(x)",1,"s") #this function fills up the "fig" imported from other graph


win.show_all()
Gtk.main()



