# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального
# окружения и PIP


from tkinter import messagebox
from tkinter import *
import random


board = Tk()
board.title("X & O")

field = []
main = random.choice('X' 'O')
sign = 0

for row in range(3):
    table = []
    for col in range(3):
        button = Button(board, text=' ', width=20, height=10,
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        table.append(button)
    field.append(table)


def click(row, col):
    global main
    if field[row][col]['text'] == ' ' and main == 'X':
        field[row][col]['text'] = 'X'
        if check_win('X'):
            box = messagebox.showinfo('***Победа***', 'Победил X')
        main = 'O'

    if field[row][col]['text'] == ' ' and main == 'O':
        field[row][col]['text'] = 'O'
        if check_win('O'):
            box = messagebox.showinfo('Победа', 'Победил O')
        main = 'X'


def check_win(cr):
    global sign

    for i in range(3):
        if field[i][0]['text'] == cr and field[i][1]['text'] == cr and field[i][2]['text'] == cr:
            sign = 1
            break
        if field[0][i]['text'] == cr and field[1][i]['text'] == cr and field[2][i]['text'] == cr:
            sign = 1
            break

    if field[0][0]['text'] == cr and field[1][1]['text'] == cr and field[2][2]['text'] == cr:
        sign = 1

    elif field[2][0]['text'] == cr and field[1][1]['text'] == cr and field[0][2]['text'] == cr:
        sign = 1

    return sign


board.mainloop()
