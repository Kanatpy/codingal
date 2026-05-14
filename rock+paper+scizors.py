from tkinter import *
from random import choice

window = Tk()
window.geometry("400x400")

def winner_loser():
    user = user_choice.get().lower()
    comp = choice(["rock", "paper", "scissors"])

    result_label.config(text=f"Computer chose: {comp}")

    if user == comp:
        outcome_label.config(text="It's a tie!")
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        outcome_label.config(text="You win!")
    elif user in ["rock", "paper", "scissors"]:
        outcome_label.config(text="Computer wins!")
    else:
        outcome_label.config(text="Invalid input!")

r_p_s = Label(text="Rock, Paper, Scissors")
user_choice = Entry()
result_label = Label(text="")
outcome_label = Label(text="")

play = Button(text="Play", command=winner_loser)

r_p_s.pack()
user_choice.pack()
play.pack()
result_label.pack()
outcome_label.pack()

window.mainloop()