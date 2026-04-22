from tkinter import *

def calculate():
    try:
        # Get values from input boxes and convert to numbers
        n1 = float(first_num.get())
        n2 = float(second_num.get())
        # Update the result label
        result_lbl.config(text=f"{n1 + n2}")
    except ValueError:
        result_lbl.config(text="Please enter valid numbers")
window = Tk()
window.title("Kinda a Calculator")
window.geometry("300x300")
lbl1 = Label(window, text="First Number")
lbl1.pack()
first_num = Entry(window, width=10)
first_num.pack()
lbl2 = Label(window, text="Second Number")
lbl2.pack()
second_num = Entry(window, width=10)
second_num.pack()
btn = Button(window, text="Calculate", command=calculate)
btn.pack(pady=10)
result_lbl = Label(window, text="Result will appear here")
result_lbl.pack()
window.mainloop()
