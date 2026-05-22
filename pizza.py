import tkinter as tk
from tkinter import messagebox

class pizzashopui:
    def __init__(self,root):
        self.root= root
        self.root.title("PIZZA")
        self.root.geometry("400x400")

        self.sizes = {"small":0.01,"medium":10,"large":10000000}
        self.crusts = {"thin":1,"CHEZZY":100,"classic":0}
        self.toppings = {"pepperoni":50,"cheese":50,"olives":25}

        self.sizVar =tk.StringVar(value="medium")
        self.crustVar = tk.StringVar(value="classic")
        self.toppingsVar = {t:tk.IntVar() for t in self.toppings}

        tk.Label(root,text="Pizza Size:",font=("ariel",12,"bold")).pack(anchor="w")
        
        for size in self.sizes:
            tk.Radiobutton(root,text=f"{size} - ${self.sizes[size]}",variable=self.sizVar,value=size).pack(anchor="w")

        tk.Label(root,text="Toppings:",font=("ariel",12,"bold"))    
        for topping in self.toppings:
            tk.Radiobutton(root,text=f"{topping} - ${self.toppings[topping]}",variable=self.toppingsVar,value=self.toppings).pack(anchor="w")

        tk.Button(root,text="order",command = self.show_bill,bg="green",fg="white" ,font=("ariel",12,"bold")).pack(pady=10)

    def show_bill(self):
        total = self.sizes[self.sizVar.get()] +self.crusts[self.crustVarVar.get()]
        chosen_topps = [t for t,var in self.toppingsVar.items() if var.get() == 1]
        for t in chosen_topps:
            total += self.toppings[t]
        orderSummery = f"pizza\n size: {self.sizVar.get()}\ncrust: {self.crustVar.get()}\n"
        orderSummery += f"toppings: {', '.join(chosen_topps) if chosen_topps else "nonn"}\n"
        orderSummery += f"total bill: ${total}"

        messagebox.showinfo("Order Summery" , orderSummery)

root = tk.Tk()
app=pizzashopui(root)
root.mainloop()
