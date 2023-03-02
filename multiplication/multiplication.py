from tkinter import *
from PIL import ImageTk, Image
import random

main = Tk()
main.title("Multiplication")
#main.iconbitmap(".ico")

correctscore = 0
wrongscore = 0

def randomize():
    global answer
    set_difficulty = (str(horizontal_slider.get()))
    if set_difficulty == str(0):
        first_num = random.randint(1, 9)
        second_num = random.randint(1, 9)
        first_num_label = Label(mainframe, text="      " + str(first_num) + "       ").grid(row=0, column=0)
        second_num_label = Label(mainframe, text="      " + str(second_num) + "       ").grid(row=0, column=2)
        answer = (first_num * second_num)
        check_answer = Button(main, text="Answer", command=compare_answer, width=14).grid(row=1, column=2, padx=10)

    elif set_difficulty == str(1):
        first_num = random.randint(1, 99)
        second_num = random.randint(1, 99)
        first_num_label = Label(mainframe, text="     " + str(first_num) + "      ").grid(row=0, column=0)
        second_num_label = Label(mainframe, text="     " + str(second_num) + "      ").grid(row=0, column=2)
        answer = (first_num * second_num)
        check_answer = Button(main, text="Answer", command=compare_answer, width=14).grid(row=1, column=2, padx=10)

    elif set_difficulty == str(2):
        first_num = random.randint(1, 999)
        second_num = random.randint(1, 999)
        first_num_label = Label(mainframe, text="    " + str(first_num) + "    ").grid(row=0, column=0)
        second_num_label = Label(mainframe, text="    " + str(second_num) + "     ").grid(row=0, column=2)
        answer = (first_num * second_num)
        check_answer = Button(main, text="Answer", command=compare_answer, width=14).grid(row=1, column=2, padx=10)

    elif set_difficulty == str(3):
        first_num = random.randint(1, 9999)
        second_num = random.randint(1, 9999)
        first_num_label = Label(mainframe, text="   " + str(first_num) + "   ").grid(row=0, column=0)
        second_num_label = Label(mainframe, text="   " + str(second_num) + "  ").grid(row=0, column=2)
        answer = (first_num * second_num)
        check_answer = Button(main, text="Answer", command=compare_answer, width=14).grid(row=1, column=2, padx=10)

    elif set_difficulty == str(4):
        first_num = random.randint(1, 99999)
        second_num = random.randint(1, 99999)
        first_num_label = Label(mainframe, text="  " + str(first_num) + "  ").grid(row=0, column=0)
        second_num_label = Label(mainframe, text="  " + str(second_num) + "  ").grid(row=0, column=2)
        answer = (first_num * second_num)
        check_answer = Button(main, text="Answer", command=compare_answer, width=14).grid(row=1, column=2, padx=10)

    elif set_difficulty == str(5):
        first_num = random.randint(1, 999999)
        second_num = random.randint(1, 999999)
        first_num_label = Label(mainframe, text=" " + str(first_num) + " ").grid(row=0, column=0)
        second_num_label = Label(mainframe, text=" " + str(second_num) + " ").grid(row=0, column=2)
        answer = (first_num * second_num)
        check_answer = Button(main, text="Answer", command=compare_answer, width=14).grid(row=1, column=2, padx=10)

    else:
        first_num = random.randint(1, 9999999)
        second_num = random.randint(1, 9999999)
        first_num_label = Label(mainframe, text=first_num).grid(row=0, column=0)
        second_num_label = Label(mainframe, text=second_num).grid(row=0, column=2)
        answer = (first_num * second_num)
        check_answer = Button(main, text="Answer", command=compare_answer, width=14).grid(row=1, column=2, padx=10)


def compare_answer():
    global player_answer, answer, correctscore, wrongscore
    player_answer = answer_enty.get()
    if int(player_answer) == answer:
        score_announcement = Label(answer_frame, text="Correct").grid(row=0, column=1)
        correctscore += 1
        correctscore_label = Label(answer_frame, text="Correct score " + str(correctscore)).grid(row=0, column=0)
        wrongscore_label = Label(answer_frame, text="Wrong score " + str(wrongscore)).grid(row=1, column=0)
        check_answer = Button(main, text="Answer", command=alreadyanswered, width=14).grid(row=1, column=2, padx=10)

    else:
        score_announcement = Label(answer_frame, text="Wrong  ").grid(row=0, column=1)
        wrongscore += 1
        correctscore_label = Label(answer_frame, text="Correct score " + str(correctscore)).grid(row=0, column=0)
        wrongscore_label = Label(answer_frame, text="Wrong score " + str(wrongscore)).grid(row=1, column=0)
        check_answer = Button(main, text="Answer", command=alreadyanswered, width=14).grid(row=1, column=2, padx=10)


def alreadyanswered():
    check_answer = Button(main, text="Create new values", width=14).grid(row=1, column=2, padx=10)

    # Objects
mainframe = LabelFrame(main, padx=20, pady=20)

first_num_label = Label(mainframe, text="                   ").grid(row=0, column=0)
multiplier_label = Label(mainframe, text=" x ").grid(row=0, column=1)
second_num_label = Label(mainframe, text="                   ").grid(row=0, column=2)

answer_enty = Entry(main)

# Difficulty slider
difficulty_label = Label(main, text="Difficulty").grid(row=0, column=0)
horizontal_slider = Scale(main, from_=0, to=6, orient=HORIZONTAL)
randomize_button = Button(main, text="Randomize", command=randomize, width=14).grid(row=0, column=2, padx=10)

answer_frame = LabelFrame(main, padx=200, pady=30)
check_answer = Button(main, text="Answer", command=alreadyanswered, width=14).grid(row=1, column=2, padx=10)

# Placement
mainframe.grid(row=1, column=0)

horizontal_slider.grid(row=0, column=1)
answer_enty.grid(row=1, column=1, padx=50)

answer_frame.grid(row=2, column=0, pady=10, columnspan=3)


main.mainloop()
