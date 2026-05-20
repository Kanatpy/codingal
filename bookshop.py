import tkinter as tk
from tkinter import messagebox

class Bookshop:
    def __init__(self,root):
        self.root = root
        self.root.title("Bookshop managment")
        self.root.geometry("600x400")
        self.books = []

        tk.Label(root,text="Bookshop management" ,font=("Ariel",18,"bold")).pack(pady=10)
        frame=tk.Frame(root)
        frame.pack(pady=10)
        tk.Label(frame,text="Title:").grid(row=0,column=0,padx=5,pady=5)
        self.title_entry = tk.Entry(frame)
        self.title_entry.grid(row=0,column=1,padx=5,pady=5)
        tk.Label(frame,text="Author:").grid(row=1,column=0,padx=5,pady=5)
        self.author_entry = tk.Entry(frame)
        self.author_entry.grid(row=1,column=1,padx=5,pady=5)
        tk.Label(frame,text="Price:").grid(row=2,column=0,padx=5,pady=5)
        self.price_entry = tk.Entry(frame)
        self.price_entry.grid(row=2,column=1,padx=5,pady=5)
        tk.Button(frame,text="Add book",command=self.add_book).grid(row=3,column=0,pady=10)
        tk.Button(frame,text="View Inventory",command=self.view_books).grid(row=3,column=1,pady=10)
        self.list_box = tk.Listbox(root,width=70,height=10)
        self.list_box.pack(pady=10)
        tk.Button(root,text='Purchase the book',command=self.purchase).pack(pady=5)
    def add_book(self):
        title=self.title_entry.get()
        author = self.author_entry.get()
        price = self.price_entry.get()

        if title and author and price:
            try:
                price = float(price)
                self.books.append({f"title: {title}, author:{author}, price: {price}"})
                messagebox.showinfo("Success",f"Book {title} added")
                self.title_entry.delete(0,tk.END)
                self.author_entry.delete(0,tk.END)
                self.price_entry.delete(0,tk.END)
            except ValueError:
                messagebox.showerror("ERROR!","Wrong Value of Price")
        else:
            messagebox.showerror("ERROR!","All feilds are required")
    def view_books(self):
        self.listbox.delete(0, tk.END)
        for idx, book in enumerate(self.books, start=1):
            self.listbox.insert(tk.END, f"{idx}. {book['title']} by {book['author']} - ₹{book['price']}")

    def purchase(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            book = self.books[index]
            messagebox.showinfo("Purchase", f"You purchased '{book['title']}' for ₹{book['price']}")
            del self.books[index]
            self.view_books()
        else:
            messagebox.showerror("Error", "Select a book to purchase")


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = Bookshop(root)
    root.mainloop()
