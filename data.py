from pathlib import PureWindowsPath
import random
import emoji
from turtle import *
mod = 120
import turtle
square = turtle.Turtle()
square.shape("classic")
turtle.pensize(5)
turtle.speed(0)


def new_screen():
    turtle.pencolor('black')
    for i in range(-1,2,2):
        penup()
        setpos(-mod*1.5,mod/2*i)
        pendown()
        setpos(mod*1.5,mod/2*i)
        penup()
        setpos(mod/2*i,-mod*1.5)
        pendown()
        setpos(mod/2*i,mod*1.5)
        penup()

def circle(pos):
    turtle.pencolor('red')
    xpos = ((2 + pos)% 3) * mod -mod
    ypos = -((pos -1) // 3)*mod + mod*0.75
    penup()
    setpos(xpos, ypos)
    pendown()
    turtle.circle(mod/3)
    penup()

def cross(pos):
    turtle.pencolor('blue')
    xpos = ((2 + pos)% 3) * mod -mod
    ypos = -((pos -1) // 3)*mod + mod
    setpos(xpos-mod/3, ypos-mod/3)
    pendown()
    setpos(xpos + mod/3, ypos + mod/3)
    penup()
    setpos(xpos-mod/3, ypos + mod/3-5)
    pendown()
    setpos(xpos + mod/3-5, ypos - mod/3)
    penup()

def demo():
    new_screen()
    for i in range(1,9,2):
        cross(i)
        circle(random.randint(1,9))

def get_pos(x, y):
    if -mod*1.5 < x < -mod*0.5:
        pos = 1
    elif -mod*0.5 < x < mod*0.5:
        pos = 2
    elif mod*0.5 < x < mod*1.5:
        pos = 3
    else: return 4
    if -mod*1.5 < y < -mod*0.5:
        pos = pos + 6
    elif -mod*0.5 < y < mod*0.5:
        pos = pos + 3
    elif mod*0.5 < y < mod*1.5:
        pos = pos
    else: return 7
    cross(pos)

def new_board(lst):
    for i in range(3):
        for j in range(3):
            if lst[i*3+j] == 'X':

                print(emoji.emojize(' :crossed_swords: |'), end='')
            elif lst[i*3+j] == 'O':
                print(emoji.emojize(' :egg:|'), end='')
            else:    
                print(' ' + lst[i*3+j] + ' |', end='')
        print('\n------------')

def pl_turn(lst, player_token):
    print('\n Ваш ход...')
    valid = False
    while not valid:
        move = int(input("Куда поставим " + player_token+"? "))
        if 1 <= move <= 9:
            if lst[move-1] not in "XO":
                lst[move-1] = player_token
                valid = True
            else:
                print ("Эта клетка уже занята")
        else: print('Число за пределами границ, попробуйте еще')

def comp_turn(lst, comp_token):
    print('\n Ход компьютера...')
    move = random.randint(0,8)
    while lst[move] in "XO":
        move = random.randint(0,8)
    lst[move] = comp_token

def check_board(lst):
    if lst[0] == lst[1] and lst[1] == lst[2]:
        x=True
        return x
    elif lst[3] == lst[4] and lst[4] == lst[5]:
        x=True
        return x
    elif lst[6] == lst[7] and lst[7] == lst[8]:
        x=True
        return x
    elif lst[0] == lst[3] and lst[3] == lst[6]:
        x=True
        return x
    elif lst[1] == lst[4] and lst[4] == lst[7]:
        x=True
        return x
    elif lst[2] == lst[5] and lst[5] == lst[8]:
        x=True
        return x
    elif lst[0] == lst[4] and lst[4] == lst[8]:
        x=True
        return x
    elif lst[2] == lst[4] and lst[4] == lst[6]:
        x=True
        return x

def game(board, player_token, comp_token):
    x = False
    counter = 0 
    if player_token == 'X':
        new_board(board)
        winner = comp_token
        while not x:
            pl_turn(board, player_token)
            new_board(board)
            x = check_board(board)
            if x == True:
                winner = player_token
                break
            counter +=1
            if counter == 9: 
                print('Ничья!')
                break
            comp_turn(board, comp_token)
            new_board(board)
            x = check_board(board)
            counter +=1
            if counter == 8: print('Ничья!')
    else:
        winner = player_token
        while not x:
            comp_turn(board, comp_token)
            new_board(board)
            x = check_board(board)
            if x == True:
                winner = comp_token
                break
            counter +=1
            if counter == 9: print('Ничья!')
            pl_turn(board, player_token)
            new_board(board)
            x = check_board(board)
            counter +=1
    print('Конец! Выиграли ' + winner)

demo()
exitonclick()