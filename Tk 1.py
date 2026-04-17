import tkinter as tk
from datetime import date

window = tk.Tk()
window.title("window")
window.geometry("400x400")

lbl = tk.Label(window,text="something",fg="white",bg="#0B2FB1",height=1,width=400)

nameLbl = tk.Label(text="Full name",bg="#096561")
nameEntry = tk.Entry()

def display():
    name = nameEntry.get()
    global message
    message = "welcome to something"
    greet = "Hello "+name+"\n"
    text_box.insert(tk.END,greet)
    text_box.insert(tk.END,message+"\n")
    text_box.insert(tk.END,date.today())

text_box = tk.Text(height=3)

btn = tk.Button(text="began",command=display,height=1,bg="#711515",fg="white")

lbl.pack()
nameLbl.pack()
nameEntry.pack()
btn.pack()
text_box.pack()
tk.mainloop()