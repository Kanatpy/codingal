from tkinter import *

root = Tk()
root.geometry("300x300")

def convert():
    e = inches.get()
    inches1 = float(e)*2.54
    centimeters = Label(root,text=inches1)
    centimeters.pack()
inches = Entry()
inches_label = Label(text="inches")
#inches1 = float(inches.get())*2.54
convert_button = Button(text="Convert",command=convert)
inches_label.pack()
inches.pack()
convert_button.pack()

root.mainloop()