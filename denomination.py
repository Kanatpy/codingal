from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

root = Tk()
root.title("denomination calc")
root.configure(bg="light blue")
root.geometry("650x400")

upload = Image.open("money.jpg")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)

image_label = Label(root,image=image,bg="light blue")
image_label.place(x=180,y=20)

label1 = Label(root,text="Hi!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",bg="light blue")
label1.place(relx=0.5,y=340,anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo("alert","HHihIihIHIHIHIHiHi!!!!!!!!!")
    if MsgBox == "ok":
        topwin()

button1 = Button(root,text="START NOW!!!!!!!",command=msg,bg="red",fg="white")
button1.place(x=260,y=360)

def topwin():
    top = Toplevel()
    top.title("actual dem. calculaotr")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")
    label = Label(top,text="enter total amount",bg="light grey")
    entry = Entry(top)
    lbl = Label(top,text="nums",bg="light grey")

    l1 = Label(top,text="100",bg="light grey")
    l2 = Label(top,text="50",bg="light grey")
    l3 = Label(top,text="20",bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():

        try:

            amount = int(entry.get())

            note2000 = amount // 2000

            amount %= 2000

            note500 = amount // 500

            amount %= 500

            note100 = amount // 100

            t1.delete(0, END)

            t2.delete(0, END)

            t3.delete(0, END)

            t1.insert(END, str(note2000))

            t2.insert(END, str(note500))

            t3.insert(END, str(note100))

        except ValueError:

            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(

    top,

    text="Calculate",

    command=calculator,

    bg="brown",
    fg="white"

    )

# -------------------------------

# Placing Widgets

# -------------------------------

    label.place(x=230, y=50)

    entry.place(x=200, y=80)

    btn.place(x=240, y=120)

    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)

    l2.place(x=180, y=230)

    l3.place(x=180, y=260)

    t1.place(x=270, y=200)

    t2.place(x=270, y=230)

    t3.place(x=270, y=260)

    top.mainloop()

# -------------------------------

# Start Main Loop

# -------------------------------

root.mainloop()