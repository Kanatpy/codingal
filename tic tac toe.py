board = {'7': ' ' , '8': ' ' , '9': ' ' ,

'4': ' ' , '5': ' ' , '6': ' ' ,

'1': ' ' , '2': ' ' , '3': ' ' }
board_keys = []

for key in board:
    board_keys.append(key)

def printBoard(board):

    print(board['7'] + '|' + board['8'] + '|' + board['9'])

    print('-+-+-')

    print(board['4'] + '|' + board['5'] + '|' + board['6'])

    print('-+-+-')

    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = "X"
    count =0

    for i in range(10):
        printBoard(board)
        print("its your turn\n turn:",turn)

        move = input()

        if board[move] == " ":
            board[move] = turn
            count+=1
        else:
            print("already filled")
            continue
            
        if count >= 5:

            if board['7'] == board['8'] == board['9'] != ' ': # across the top
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif board['4'] == board['5'] == board['6'] != ' ': # across the top
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif board['1'] == board['2'] == board['3'] != ' ': # across the top
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif board['3'] == board['5'] == board['7'] != ' ': # across the top
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif board['9'] == board['5'] == board['1'] != ' ': # across the top
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif board['8'] == board['5'] == board['2'] != ' ': # across the top
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif board['7'] == board['4'] == board['1'] != ' ': # across the top
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif board['9'] == board['6'] == board['3'] != ' ': # across the top
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
        if count  == 9:
            print("Tie")
        if turn == "X":
            turn ="O"
        else:
            turn = "X"
    restart = input("wanna play again: y/n")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            board[key] = " "
        game()
    else:
        print("next time then")
if __name__ == "__main__":
    game()

