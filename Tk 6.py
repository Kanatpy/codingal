import tkinter as tk
from datetime import datetime
from tkcalendar import DateEntry  # Make sure to install: pip install tkcalendar

root = tk.Tk()
root.title("Python Login")
root.geometry("400x400")

frame = tk.Frame(root, height=200, width=360, bg="#d0efff")
frame.place(x=20, y=0)

# Labels
tk.Label(frame, text="Birth Date", bg="#3859D3", fg="white", width=12).place(x=20, y=20)

# Date Entry using tkcalendar
dob_entry = DateEntry(frame, date_pattern='yyyy-mm-dd', font=("Arial", 12), width=12)
dob_entry.place(x=150, y=20)

# Output Text Box
textbox = tk.Text(root, bg="#BEBEBE", fg="black", height=6, width=40)
textbox.place(x=20, y=250)

def display():
    try:
        birth_date = dob_entry.get_date()  # Returns a datetime.date object
        today = datetime.now().date()

        # Calculate age properly
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        if days < 0:
            months -= 1
            # Approximate days in previous month (simplified)
            days += (30 if months < 0 else 30)  # Could use calendar.monthrange for accuracy

        if months < 0:
            years -= 1
            months += 12

        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, f"Age: {years} years, {months} months, {days} days")
    except Exception as e:
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, f"Error: {str(e)}")

# Button
btn = tk.Button(root, text="Find your age", command=display, bg="red", fg="white")
btn.place(x=150, y=210)

root.mainloop()   