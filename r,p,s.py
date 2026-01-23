from random import choice
while True:
    user_action = input("enter rock paper or scissors: ")
    possible_actions = ["rock","paper","scissors"]
    comp_action = choice(possible_actions)
    print(f"\nYou chose {user_action}, comp chose {comp_action}.\n")

    if user_action == comp_action:
        print("tie")

    elif user_action == "rock":
        if comp_action == "paper":
            print("comp wins")
        else:
            print("you win")

    elif user_action == "scissors":
        if comp_action == "rock":
            print("comp wins")
        else:
            print("you win")

    elif user_action == "paper":
        if comp_action == "rock":
            print("comp wins")
        else:
            print("you win")

    play_again = input("play again? y or n: ")
    if play_again == "n" or play_again == "no":
        break