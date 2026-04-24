from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("ALERT","You Have Bad Taste!!!")
    lbl.pack()
lbl = Label(text="didnt work you still have bad taste",bg="red")
button = Button(root,text="have better taste",command=msg)

button.place(x=40,y=80)

root.mainloop()