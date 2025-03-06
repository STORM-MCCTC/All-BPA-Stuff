import random

# Initialize the board positions (empty spaces are represented as "#")
c1 = "#"
c2 = "#"
c3 = "#"
b1 = "#"
b2 = "#"
b3 = "#"
a1 = "#"
a2 = "#"
a3 = "#"

#-----------------
# "c1","c2","c3"
# "b1","b2","b3"
# "a1","a2","a3"
#-----------------

# Function to print the current state of the board
def print_board():
    # Print the board in a readable format
    print(f'''
       C {c1} {c2} {c3}
       B {b1} {b2} {b3}
       A {a1} {a2} {a3}
         1 2 3   
           ''')

# Function to handle player's move
def move_func():
    global c1, c2, c3, b1, b2, b3, a1, a2, a3
    move = "null"
    
    # Prompt the player for their move
    move = input("move: ")

    # Check if the player's move is valid (empty space and valid position)
    if a1 != "O" and move.lower() == "a1":
        a1 = "X"
    elif a2 != "O" and move.lower() == "a2":
        a2 = "X"
    elif a3 != "O" and move.lower() == "a3":
        a3 = "X"
    elif b1 != "O" and move.lower() == "b1":
        b1 = "X"
    elif b2 != "O" and move.lower() == "b2":
        b2 = "X"
    elif b3 != "O" and move.lower() == "b3":
        b3 = "X"
    elif c1 != "O" and move.lower() == "c1":
        c1 = "X"
    elif c2 != "O" and move.lower() == "c2":
        c2 = "X"
    elif c3 != "O" and move.lower() == "c3":
        c3 = "X"
    else:
        # If the move is invalid (position already taken), ask the player to try again
        print("Invalid move. Try again.")
        move_func()

# Function to handle computer's move (random choice)
def com_move_func():
    global c1, c2, c3, b1, b2, b3, a1, a2, a3
    com_move = "null"
    
    # List of possible moves for the computer
    move_list = ["c1", "c2", "c3", "b1", "b2", "b3", "a1", "a2", "a3"]
    
    # Randomly pick a valid move for the computer
    com_move = random.choice(move_list)

    # Check if the spot is available and then place "O" for the computer
    if a1 != "X" and com_move == "a1":
        a1 = "O"
    elif a2 != "X" and com_move == "a2":
        a2 = "O"
    elif a3 != "X" and com_move == "a3":
        a3 = "O"
    elif b1 != "X" and com_move == "b1":
        b1 = "O"
    elif b2 != "X" and com_move == "b2":
        b2 = "O"
    elif b3 != "X" and com_move == "b3":
        b3 = "O"
    elif c1 != "X" and com_move == "c1":
        c1 = "O"
    elif c2 != "X" and com_move == "c2":
        c2 = "O"
    elif c3 != "X" and com_move == "c3":
        c3 = "O"
    else:
        # If the chosen spot is invalid, call the function again (recursive call)
        com_move_func()

# Function to check if a player has won the game
def check_winner(player):
    # Check all rows for a winning condition
    if (a1 == a2 == a3 == player) or (b1 == b2 == b3 == player) or (c1 == c2 == c3 == player):
        return True
    # Check all columns for a winning condition
    elif (a1 == b1 == c1 == player) or (a2 == b2 == c2 == player) or (a3 == b3 == c3 == player):
        return True
    # Check both diagonals for a winning condition
    elif (a1 == b2 == c3 == player) or (a3 == b2 == c1 == player):
        return True
    return False

# Function to check if the game has ended in a draw (no empty spots left)
def check_draw():
    # If there are no more "#" spots on the board, the game is a draw
    if all([x != "#" for x in [a1, a2, a3, b1, b2, b3, c1, c2, c3]]):
        return True
    return False
    
# Game loop: continuously runs the game until a winner or draw is found
while True:
    print_board()  # Display the current board state
    
    move_func()  # Ask the player for a move
    
    # Check if the player ("X") has won the game
    if check_winner("X"):
        print_board()  # Print final board
        print("X wins!")  # Announce player win
        break  # Exit the game loop
    
    # Check if the game is a draw
    if check_draw():
        print_board()  # Print final board
        print("It's a draw!")  # Announce draw
        break  # Exit the game loop
    
    com_move_func()  # Ask the computer to make a move
    
    # Check if the computer ("O") has won the game
    if check_winner("O"):
        print_board()  # Print final board
        print("O wins!")  # Announce computer win
        break  # Exit the game loop
    
    # Check if the game is a draw
    if check_draw():
        print_board()  # Print final board
        print("It's a draw!")  # Announce draw
        break  # Exit the game loop
