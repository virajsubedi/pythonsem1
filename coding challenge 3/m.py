import random
import os.path
import json
random.seed()

fromimport *

    
def main():
    board = [ ['1','2','3'],\
              ['4','5','6'],\
              ['7','8','9']]

    welcome(board)
    total_score = 0
    while True:
        choice = menu()
        if choice == '1':
            score = play_game(board)
            total_score += score
            print('Your current score is:',total_score)
        if choice == '2':
            save_score(total_score)
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return



def draw_board(board):
   for row in board:
    print("|".join(row))

def welcome(board):
  print("Welcome to Tic-Tac-Toe!")
  draw_board(board)

def initialise_board(board):
   for i in range(3):
    for j in range(3):
     board[i][j] = " "
   return board

def get_player_move(board):
   valid_input = False
   while not valid_input:
    row = int(input("Please enter the row for your move (1-3): ")) - 1
    col = int(input("Please enter the column for your move (1-3): ")) - 1
    if row in range(3) and col in range(3) and board[row][col] == " ":
     valid_input = True
    else:
     print("Invalid move, please try again.")
    return row, col

def choose_computer_move(board):
   available_moves = []
   for i in range(3):
    for j in range(3):
     if board[i][j] == " ":
      available_moves.append((i, j))
      return random.choice(available_moves)

def check_for_win(board, mark):
  # check rows
  for row in board:
    if row[0] == mark and row[1] == mark and row[2] == mark:
      print('you win')
      return True
  # check columns
  for i in range(3):
    if board[0][i] == mark and board[1][i] == mark and board[2][i] == mark:
      print('you win')
      return True
  # check diagonals
  if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
    print('you win')
    return True
  if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
    print('you win')
    return True
  return False

def check_for_draw(board):
  for row in board:
    for cell in row:
      if cell == " ":
        return False
  return True

def play_game(board):
  initialise_board(board)
  draw_board(board)
  while True:
    row, col = get_player_move(board)
    board[row][col] = "X"
    draw_board(board)
    if check_for_win(board, "X"):
      return 1
    if check_for_draw(board):
      return 0
    row, col = choose_computer_move(board)
    board[row][col] = "O"
    draw_board(board)
    if check_for_win(board, "O"):
      return -1
    if check_for_draw(board):
      return 0

def menu():
  choice = input("Please enter 1 to play, 2 to save score, 3 to view leaderboard, or q to quit: ")
  if choice==1:
    play_game(board)
  elif choice==2:
    save_score(score)
  elif choice==3:
    display_leaderboard(leaders)
  elif choice=='q':
    print('Thank you for playing')
  return choice
def load_scores():
  leaders = {}
  if os.path.exists("leaderboard.txt"):
    with open("leaderboard.txt", "r") as file:
      leaders = json.load(file)
  return leaders

def save_score(score):
  name = input("Enter your name: ")
  leaders = load_scores()
  leaders[name] = score
  with open("leaderboard.txt", "w") as file:
    json.dump(leaders, file)

def display_leaderboard(leaders):
  print("LEADERBOARD")
  for name, score in leaders.items():
    print(f"{name}: {score}")

