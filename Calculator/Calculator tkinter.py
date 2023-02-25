from tkinter import *

calc = Tk()
calc.title("Calculator")


def button_click(number):
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current) + str(number))
    return


def clear():
    screen.delete(0, END)
    return


def plus():
    first_number = screen.get()
    global f_num
    global math
    math = "plus"
    f_num = float(first_number)
    screen.delete(0, END)
    return


def minus():
    first_number = screen.get()
    global f_num
    global math
    math = "minus"
    f_num = float(first_number)
    screen.delete(0, END)
    return


def divide():
    first_number = screen.get()
    global f_num
    global math
    math = "divide"
    f_num = float(first_number)
    screen.delete(0, END)
    return


def multiply():
    first_number = screen.get()
    global f_num
    global math
    math = "multiply"
    f_num = float(first_number)
    screen.delete(0, END)
    return


def equals():
    second_number = screen.get()
    screen.delete(0, END)

    if math == "plus":
        screen.insert(0, float(f_num) + float(second_number))

    if math == "minus":
        screen.insert(0, float(f_num) - float(second_number))

    if math == "divide":
        screen.insert(0, float(f_num) / float(second_number))

    if math == "multiply":
        screen.insert(0, float(f_num) * float(second_number))

    return


screen = Entry(calc, width=50, borderwidth=5)
button_1 = Button(calc, text="1", padx=30, pady=10, command=lambda: button_click(1))
button_2 = Button(calc, text="2", padx=30, pady=10, command=lambda: button_click(2))
button_3 = Button(calc, text="3", padx=30, pady=10, command=lambda: button_click(3))
button_4 = Button(calc, text="4", padx=30, pady=10, command=lambda: button_click(4))
button_5 = Button(calc, text="5", padx=30, pady=10, command=lambda: button_click(5))
button_6 = Button(calc, text="6", padx=30, pady=10, command=lambda: button_click(6))
button_7 = Button(calc, text="7", padx=30, pady=10, command=lambda: button_click(7))
button_8 = Button(calc, text="8", padx=30, pady=10, command=lambda: button_click(8))
button_9 = Button(calc, text="9", padx=30, pady=10, command=lambda: button_click(9))
button_0 = Button(calc, text="0", padx=30, pady=10, command=lambda: button_click(0))
buttonMinus = Button(calc, text="-", padx=30, pady=10, command=minus)
buttonPlus = Button(calc, text="+", padx=30, pady=10, command=plus)
buttonDivide = Button(calc, text="/", padx=30, pady=10, command=divide)
buttonMultiply = Button(calc, text="*", padx=30, pady=10, command=multiply)
buttonEquals = Button(calc, text="=", padx=29, pady=10, command=equals)
buttonDecimal = Button(calc, text=".", padx=31, pady=10, command=lambda: button_click("."))
buttonClear = Button(calc, text="Clear", padx=20, pady=80, command=clear)

screen.grid(row=00, column=0, columnspan=4)
buttonClear.grid(row=2, column=3, rowspan=4)
buttonDivide.grid(row=1, column=0)
buttonMultiply.grid(row=1, column=1)
buttonMinus.grid(row=1, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
buttonPlus.grid(row=1, column=3)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
buttonEquals.grid(row=5, column=2)
button_0.grid(row=5, column=0)
buttonDecimal.grid(row=5, column=1)

calc.mainloop()
