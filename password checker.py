from tkinter import *
import string

root = Tk()
root.geometry("300x300")

# Create one label to update instead of making new ones every click
result_label = Label(root, text="")
result_label.pack(side=BOTTOM)

def check():
    password = p.get()
    
    # 1. Specific "easter egg" check first
    if password == "67":
        result_label.config(text="67", fg="blue")
    
    # 2. Check if it contains at least one of EACH requirement for a "great" password
    elif (any(c in string.punctuation for c in password) and 
          any(c in string.ascii_letters for c in password) and 
          any(c in string.digits for c in password)):
        result_label.config(text="great password", fg="green")
        
    # 3. If it has some characters but didn't meet all three requirements above
    elif any(c in (string.punctuation + string.ascii_letters + string.digits) for c in password):
        result_label.config(text="not good enough", fg="orange")
        
    # 4. If it's empty or doesn't match anything
    else:
        result_label.config(text="nahhhhhhhhhhhhhhhhhh", fg="red")

p_label = Label(text="password")
p_label.pack()

p = Entry() 
p.pack()

convert_button = Button(text="Check", command=check)
convert_button.pack()

root.mainloop()
