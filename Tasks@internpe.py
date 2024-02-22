# 1) Tic Tac Toe Game:
'''
import random

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

# game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# take player input
def playerInput(board):
    inp = int(input("Select a spot 1-9: "))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already at that spot.")


# check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True


def checkIfWin(board):
    global gameRunning
    if checkHorizontle(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False


def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False


# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    computer(board)
    checkIfWin(board)
    checkIfTie(board)
'''
    

'''
# 2) Digital Locker;

from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")

def time():
    string = strftime('%H:%M:%S: %P')
    Label.config(text=string)
    Label.after (1000,time)

Label = Label(root, font=("ds-digital", 80), background = "black", foreground="cyan")
Label.pack(anchor='center')
time()

mainloop()

import sys
from tkinter import *
import time

def times():
    current_time=time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200,times)


root = Tk()
root.geometry("400x200")
clock=Label(root,font=("times",42,"bold"),bg="white")
clock.grid(row=2,column=2,pady=25,padx=100)
times()

digi=Label(root,text="Digital Clock",font="times 24 bold")
digi.grid(row=0,column=2)

nota=Label(root,text="hours minutes seconds ",font="times 15 bold")
nota.grid(row=3,column=2)

root.mainloop()
'''


# 3) Shutdown or reset;
import os

def shutdown():
    if os.name == "nt":  # For Windows
        os.system("shutdown /s /t 0")
    elif os.name == "posix":  # For Linux or macOS
        os.system("sudo shutdown now")
    else:
        print("Sorry, your operating system is not supported for shutdown.")
        return

def restart():
    if os.name == "nt":  # For Windows
        os.system("shutdown /r /t 0")
    elif os.name == "posix":  # For Linux or macOS
        os.system("sudo reboot")
    else:
        print("Sorry, your operating system is not supported for restart.")
        return

if __name__ == "_main_":
    print("Shutdown Project")
    print("1. Shutdown computer")
    print("2. Restart computer")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        shutdown()
    elif choice == "2":
        restart()
    else:
        print("Invalid choice. Please enter either 1 or 2.")
