'''
Passo 1: Escreva uma função que pode imprimir o tabuleiro. Configure-o como uma lista, onde cada índice 1-9 corresponde a um número em um bloco de números, para que você obtenha uma representação do tabuleiro 3 por 3.
'''
from IPython.display import clear_output
import random

def display_board(board):
   clear_output()
   print('   |   |')
   print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
   print('   |   |')
   print('-----------')
   print('   |   |')
   print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
   print('   |   |')
   print('-----------')
   print('   |   |')
   print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
   print('   |   |')
   

#print(display_board([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]))

def player_input():
   marker=' '
   while not (marker == 'X' or marker == 'O'):
     marker = input('Player1: Do you want to be X or O?').upper()
     if marker == 'X':
       return ('X', 'O')
     else:
       return ('O', 'X')

def place_marker(board, marker, position):
   board[position] = marker

def win_check(board, marker):

    return ((board[7] == marker and board[8] == marker and board[9] == marker) or # vitória pelo topo
    (board[4] == marker and board[5] == marker and board[6] == marker) or # pelo meio
    (board[1] == marker and board[2] == marker and board[3] == marker) or # por baixo
    (board[7] == marker and board[4] == marker and board[1] == marker) or # pela esquda
    (board[8] == marker and board[5] == marker and board[2] == marker) or # pelo meio
    (board[9] == marker and board[6] == marker and board[3] == marker) or # pela direita
    (board[7] == marker and board[5] == marker and board[3] == marker) or # diagonal
    (board[9] == marker and board[5] == marker and board[1] == marker)) # diagonal

def choose_first():
   if random.randint(0, 1) == 0:
     return ('Player1')
   else:
     return ('Player2')

def space_check(board, position):
   return board[position] == ' '

def full_board_check(board):
   for i in range(0, 10):
     if space_check (board, i):
       return False
     else:
       return True

def player_choice(board):
   position=' '
   while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
     position = input('Choose your move (1-9)')
   return int(position)

def replay():
   return input('Want to play again? "YES" or "NO"').lower().startwith('s')

print('Welcome to tic-tac-toe game')

while True:
# Reset Board
   theboard= [' ']*10
   player1_marker, player2_marker = player_input()
   turn = choose_first()
   print(turn+' start')
   game_on = True

   while game_on:
      if turn == 'Player1':
        display_board(theboard)
        position = player_choice(theboard)
        place_marker(theboard, player1_marker, position)
        
        if win_check(theboard, player1_marker):
          display_board(theboard)
          print('Congratulations! Your Win!')
          game_on = False
        elif full_board_check(theboard):
            display_board(theboard)
            print('Draw!')
            break
        else:
          turn = 'Player2'

   while game_on:
      if turn == 'Player2':
        display_board(theboard)
        position = player_choice(theboard)
        place_marker(theboard, player2_marker, position)

        if win_check(theboard, player2_marker):
          display_board(theboard)
          print('Congratulations! Your Win!')
          game_on = False
        elif full_board_check(theboard):
            display_board(theboard)
            print('Draw!')
            break
        else:
          turn = 'Player1'

   if not replay():
     break
