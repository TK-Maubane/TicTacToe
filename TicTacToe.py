from tkinter import *
import random

root = Tk()
root.title("My Os & Xs game")


# Checking for player 1 wins
def check_win():
    # Check for horizontal wins
    my_label = Label(root)
    if buttons[0]["text"] == "X" and buttons[1]["text"] == "X" and buttons[2]["text"] == "X":
        my_label = Label(root, text="Player 1 wins")
        my_label.grid(row=3, column=1, columnspan=3)
    elif buttons[3]["text"] == "X" and buttons[4]["text"] == "X" and buttons[5]["text"] == "X":
        my_label = Label(root, text="Player 1 wins")
        my_label.grid(row=3, column=1, columnspan=3)
    elif buttons[6]["text"] == "X" and buttons[7]["text"] == "X" and buttons[8]["text"] == "X":
        my_label = Label(root, text="Player 1 wins")
        my_label.grid(row=3, column=1, columnspan=3)

    # Check for vertical wins
    elif buttons[0]["text"] == "X" and buttons[3]["text"] == "X" and buttons[6]["text"] == "X":
        my_label = Label(root, text="Player 1 wins")
        my_label.grid(row=3, column=1, columnspan=3)
    elif buttons[1]["text"] == "X" and buttons[4]["text"] == "X" and buttons[7]["text"] == "X":
        my_label = Label(root, text="Player 1 wins")
        my_label.grid(row=3, column=1, columnspan=3)
    elif buttons[2]["text"] == "X" and buttons[5]["text"] == "X" and buttons[8]["text"] == "X":
        my_label = Label(root, text="Player 1 wins")
        my_label.grid(row=3, column=1, columnspan=3)

    # Check for diagonal wins
    elif buttons[0]["text"] == "X" and buttons[4]["text"] == "X" and buttons[8]["text"] == "X":
        my_label = Label(root, text="Player 1 wins")
        my_label.grid(row=3, column=1, columnspan=3)
    elif buttons[2]["text"] == "X" and buttons[4]["text"] == "X" and buttons[6]["text"] == "X":
        my_label = Label(root, text="Player 1 wins")
        my_label.grid(row=3, column=1, columnspan=3)

    if my_label["text"] == "Player 1 wins":
        for button in buttons:
            button["state"] = DISABLED


# Checking for computer wins
def check_comp_win():
    # Check for horizontal wins

    my_label = Label(root)
    if buttons[0]["text"] == "O" and buttons[1]["text"] == "O" and buttons[2]["text"] == "O":
        my_label = Label(root, text="Computer Wins")
        my_label.grid(row=3, column=1)
    elif buttons[3]["text"] == "O" and buttons[4]["text"] == "O" and buttons[5]["text"] == "O":
        my_label = Label(root, text="Computer Wins")
        my_label.grid(row=3, column=1)
    elif buttons[6]["text"] == "O" and buttons[7]["text"] == "O" and buttons[8]["text"] == "O":
        my_label = Label(root, text="Computer Wins")
        my_label.grid(row=3, column=1)

    # Check for vertical wins
    elif buttons[0]["text"] == "O" and buttons[3]["text"] == "O" and buttons[6]["text"] == "O":
        my_label = Label(root, text="Computer Wins")
        my_label.grid(row=3, column=1)
    elif buttons[1]["text"] == "O" and buttons[4]["text"] == "O" and buttons[7]["text"] == "O":
        my_label = Label(root, text="Computer Wins")
        my_label.grid(row=3, column=1)
    elif buttons[2]["text"] == "O" and buttons[5]["text"] == "O" and buttons[8]["text"] == "O":
        my_label = Label(root, text="Computer Wins")
        my_label.grid(row=3, column=1)

    # Check for diagonal wins
    elif buttons[0]["text"] == "O" and buttons[4]["text"] == "O" and buttons[8]["text"] == "O":
        my_label = Label(root, text="Computer Wins")
        my_label.grid(row=3, column=1)
    elif buttons[2]["text"] == "O" and buttons[4]["text"] == "O" and buttons[6]["text"] == "O":
        my_label = Label(root, text="Computer Wins")
        my_label.grid(row=3, column=1)

    if my_label["text"] == "Computer Wins":
        for button in buttons:
            button["state"] = DISABLED


# Conditions for computer to play
def comp_play():
    comp = buttons[random.randint(0, 8)]
    if comp["state"] != DISABLED:
        comp["text"] = "O"
        comp["state"] = DISABLED
    else:
        comp_play()


def pick(arg):
    buttons[arg]["state"] = DISABLED
    buttons[arg]["text"] = "X"
    check_win()
    comp_play()
    check_comp_win()


# Creating the buttons
btn_00 = Button(root, height=8, width=15, bg="powder blue", command=lambda: pick(0))
btn_01 = Button(root, height=8, width=15, bg="powder blue", command=lambda: pick(1))
btn_02 = Button(root, height=8, width=15, bg="powder blue", command=lambda: pick(2))

btn_10 = Button(root, height=8, width=15, bg="powder blue", command=lambda: pick(3))
btn_11 = Button(root, height=8, width=15, bg="powder blue", command=lambda: pick(4))
btn_12 = Button(root, height=8, width=15, bg="powder blue", command=lambda: pick(5))

btn_20 = Button(root, height=8, width=15, bg="powder blue", command=lambda: pick(6))
btn_21 = Button(root, height=8, width=15, bg="powder blue", command=lambda: pick(7))
btn_22 = Button(root, height=8, width=15, bg="powder blue", command=lambda: pick(8))

buttons = [btn_00, btn_01, btn_02, btn_10, btn_11, btn_12, btn_20, btn_21, btn_22]
# Position buttons on grid

btn_00.grid(row=0, column=0)
btn_01.grid(row=0, column=1)
btn_02.grid(row=0, column=2)

btn_10.grid(row=1, column=0)
btn_11.grid(row=1, column=1)
btn_12.grid(row=1, column=2)

btn_20.grid(row=2, column=0)
btn_21.grid(row=2, column=1)
btn_22.grid(row=2, column=2)


root.mainloop()
