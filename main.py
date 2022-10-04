import random
import emoji

from data import *

board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]


print('\nTask #4 Крестики нолики')

 


print('\bОпределяем, кто ходит первый...')
if random.random() > 0.5:
    player_token, comp_token = 'X', 'O'
else:
    player_token, comp_token = 'O', 'X'

if player_token == 'X':
    print('Ваши - ' + emoji.emojize(':crossed_swords:'))
else:
    print('Ваши - ' + emoji.emojize(':egg:'))

game(board, player_token, comp_token)

