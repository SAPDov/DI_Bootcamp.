
board = [
    ["_","_","_"],  
    ["_","_","_"],
    ["_","_","_"]
    ]
user = True #when true it X else it's O

def display_board(board):
    for row in board:
        for slot in row:
            print(f" {slot}", end="")
        print() # a new line between each row


def quit (user_input):
    if user_input.lower() == "q":
        print ("Thank you for playing")
        return True
    else:
        return False

def check_input(user_input): 
    if not check_isnum(user_input):
        return False
        print("Please choose a valid number")
    user_input = int(user_input)
    if not check_bounds(user_input): 
        return False
    else:
        return True

def check_isnum(user_input): 
    if user_input.isnumeric():
        return True
    else:
        print("Please choose a valid number")
        return False
        
def check_bounds(user_input):
    if user_input > 9 or user_input < 1:
        print("This number is out of bounds")
        return False
    else:
        return True

def isTaken(coords, board):
    row = coords[0]
    column = coords[1]
    if board[row][column] != "_":
        print("This position is already taken")
        return True
    else:
        return False

def coordinates(user_input):
    row = int(user_input / 3) 
    column = user_input 
    if column > 2:
        column = int(column % 3)
    return (row, column)

def add_to_board(coords, board, user):
    row = coords[0]
    column = coords[1]
    board[row][column] = active_user

def current_user(user):
    if user:
        return "X"
    else:
        return "O"

def is_win(user, board):
    if check_row(user, board): return True
    if check_column(user, board): return True
    if check_diag(user, board):return True
    return False

def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row: return True
    return False

def check_column(user, board):
    for col in range(3):
        complete_col = True
        for row in range (3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col: return True
    return False
def check_diag(user, board):
    if board[0][0] == user and board[1][1] == user and board[2][2] == user: return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user: return True
    else: return False

while True:
    active_user = current_user(user)
    print("TIC-TAC-TOE")
    display_board(board)
    user_input = input("Enter a position between 1-9 or enter \"q\" to quit: ")
    if quit(user_input): 
        break
    if not check_input(user_input):
        print("Please try again")
        continue
    user_input = int(user_input) - 1
    coords = coordinates (user_input)
    if isTaken(coords, board):
        print("Please try again")
        continue
    add_to_board(coords, board, user)
    if is_win(active_user, board):
        print(f"{active_user} is the winner!")
        break
    user = not user



    

