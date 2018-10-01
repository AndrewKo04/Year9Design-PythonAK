import tkinter as tk
import math

def submit():

	print("Submit pressed")
	r = float(entr.get())
	h = float(entr.get())

	v = math.pi*r*r*h
	v = round(v,3)

	output.config(state"normal")
	output.insert(tk.INSERT,v)
	output.config(state="disable")

root =tk.Tk()
root.title("Volume of a Cylinder")


labr = tk.Label(root, text="radius")
labr.pack()

entr= tk.Entry(root) #Stage 1 Construct the widget 
#Stage 2: Configure widget
entr.pack() #Stage 3: Pack the widget/element

labh = tk.Label(root, text="height")
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

output= tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()


root.mainloop()