def check_three():
    global user
    #check the rows
    for row in range(0,3):
        if board[row][0] == board[row][1] == board[row][2] == user:
            print(f"{user} won the game!")
            return True
    #check the columns
    for col in range(0, 3):
        if board[0][col] == board[1][col] == board[2][col] == user:
            print(f"{user} won the game!")
            return True

    #check the diagonals
    if board[0][0] == board[1][1] == board[2][2] == user:
        print(f"{user} won the game!")
        return True
    elif board[2][0] == board[1][1] == board[0][2] == user:
        print(f"{user} won the game!")
        return True



wants_to_play = True

while wants_to_play:
    print("Welcome to tic tac toe, do you want to play? y/n")
    response = input("\n/> ").lower()
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    while response[0] == "y":
        print("Do you want to use 'X' or 'O'? X/O")
        symbol = input("\n/> ").upper()
        if symbol == "X":
            user1 =  "X"
            user2 = "O"
            break
        elif symbol == "O":
            user1 = "O"
            user2 = "X"
            break
        else:
            continue



    #game proceeding
    count = 1
    winner = False
    while not winner and count < 10:
        print("Choose an empty slot to place your symbol.")
        if count % 2 != 0:
            user = user1
        else:
            user = user2
        row = input(f"{user} Choose the row: 0/1/2 \n/> ")
        column = input(f"{user} Choose the column: 0/1/2 \n/> ")

        if row.isdecimal() and column.isdecimal():
            if int(row) < 3 and int(column) < 3:
                if board[int(row)][int(column)] == " ":
                    board[int(row)][int(column)] = user

                    print(f"\n{board[0][0]}  | {board[0][1]}  | {board[0][2]}"
                          f"\n-----------"
                          f"\n{board[1][0]}  | {board[1][1]}  | {board[1][2]}"
                          f"\n-----------"
                          f"\n{board[2][0]}  | {board[2][1]}  | {board[2][2]}"
                          )
                    count += 1

                    if check_three():
                        winner = True
                        count = 10
                else:
                    print("Choose another cell.")
                    continue
            else:
                print("Choose a correct cell.")
                continue
        else:
            print("Choose a correct cell.")
            continue


    while True:
        print("Do you want to play again? y/n")
        play_again = input("\n/> ").lower()
        if play_again == "y":
            wants_to_play = True
            break
        elif play_again == "n":
            wants_to_play = False
            break
        else:
            continue



