from tkinter import *
from PIL import ImageTk, Image
import random

main = Tk()
main.title("Rock Paper Scissors")
main.iconbitmap("tri.ico")

p1s = ()
point1 = 0
point2 = 0
rps = [
    " Rock    ",
    " Paper   ",
    "  Scissors"
]

def player1_roll_rock():
    global p1s
    global rps
    p1s = " Rock    "
    player1_selection = Label(results, text=p1s).grid(row=1, column=0, padx=10)
    player2_roll = random.shuffle(rps)
    player2_selection = Label(results, text=rps[0]).grid(row=1, column=2)
    result_func()

def player1_roll_paper():
    global p1s
    global rps
    p1s = " Paper   "
    layer1_selection = Label(results, text=p1s).grid(row=1, column=0, padx=10)
    player2_roll = random.shuffle(rps)
    player2_selection = Label(results, text=rps[0]).grid(row=1, column=2)
    result_func()

def player1_roll_scissors():
    global p1s
    global rps
    p1s = "  Scissors"
    layer1_selection = Label(results, text=p1s).grid(row=1, column=0, padx=10)
    player2_roll = random.shuffle(rps)
    player2_selection = Label(results, text=rps[0]).grid(row=1, column=2)
    result_func()

def result_func():
    global point1
    global point2
    if p1s == rps[0]:
        final_result = Label(results, text="       Draw       ").grid(row=1, column=1)
        fill_label = Label(results, text=str(point1) + "  :  " + str(point2)).grid(row=0, column=1, padx=50, pady=10)
    elif p1s == " Rock    " and rps[0] == " Paper   ":
        final_result = Label(results, text="Player 2 Wins").grid(row=1, column=1)
        point2 += 1
        fill_label = Label(results, text=str(point1) + "  :  " + str(point2)).grid(row=0, column=1, padx=50, pady=10)
    elif p1s == " Rock    " and rps[0] == "  Scissors":
        final_result = Label(results, text="Player 1 Wins").grid(row=1, column=1)
        point1 += 1
        fill_label = Label(results, text=str(point1) + "  :  " + str(point2)).grid(row=0, column=1, padx=50, pady=10)
    elif p1s == " Paper   " and rps[0] == "  Scissors":
        final_result = Label(results, text="Player 2 Wins").grid(row=1, column=1)
        point2 += 1
        fill_label = Label(results, text=str(point1) + "  :  " + str(point2)).grid(row=0, column=1, padx=50, pady=10)
    elif p1s == " Paper   " and rps[0] == " Rock    ":
        final_result = Label(results, text="Player 1 Wins").grid(row=1, column=1)
        point1 += 1
        fill_label = Label(results, text=str(point1) + "  :  " + str(point2)).grid(row=0, column=1, padx=50, pady=10)
    elif p1s == "  Scissors" and rps[0] == " Rock    ":
        final_result = Label(results, text="Player 2 Wins").grid(row=1, column=1)
        point2 += 1
        fill_label = Label(results, text=str(point1) + "  :  " + str(point2)).grid(row=0, column=1, padx=50, pady=10)
    elif p1s == "  Scissors" and rps[0] == " Paper   ":
        final_result = Label(results, text="Player 1 Wins").grid(row=1, column=1)
        point1 += 1
        fill_label = Label(results, text=str(point1) + "  :  " + str(point2)).grid(row=0, column=1, padx=50, pady=10)



# Objects
    # Menu
menu = LabelFrame(main, padx=20, pady=20)
title_label = Label(menu, text="Rock, Paper, Scissors!!!", borderwidth=5)

rock_button = Button(menu, text="Rock", command=player1_roll_rock, width=10)
paper_button = Button(menu, text="Paper", command=player1_roll_paper, width=10)
scissors_button = Button(menu, text="Scissors", command=player1_roll_scissors, width=10)

    # Results
results = LabelFrame(main, padx=10, pady=20)
player1_label = Label(results, text="Player 1")
fill_label = Label(results, text="Score")
player2_label = Label(results, text="Player 2")

player1_selection = Label(results, text="")
player2_selection = Label(results, text="")



# Placement
    # Menu
menu.pack(padx=10, pady=10)
title_label.grid(row=0, column=0, columnspan=3, padx=50)

rock_button.grid(row=1, column=0, padx=10, pady=10)
paper_button.grid(row=1, column=1, padx=10, pady=10)
scissors_button.grid(row=1, column=2, padx=10, pady=10)

    # Results
results.pack(padx=10, pady=10)
player1_label.grid(row=0, column=0, padx=50, pady=10)
fill_label.grid(row=0, column=1, padx=50, pady=10)
player2_label.grid(row=0, column=2, padx=50, pady=10)

player1_selection.grid(row=1, column=0)




main.mainloop()
