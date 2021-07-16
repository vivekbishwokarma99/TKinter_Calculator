from tkinter import *

calc = Tk()
calc.option_add('*Font', 'Helvatica')

# Giving a title
calc.title("Calculator")
calc.geometry("360x490")
calc.iconbitmap("D:/Projects_1st_Sem/calc_1.ico")
e = Entry(calc, width=40, borderwidth=10, bg="#838996", fg="#080808", font=("Times", 12, "bold"))
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

f_num = ""
math = ""

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    global math
    math = ""
    e.delete(0, END)


def button_add():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0, END)


def button_subtract():
    first_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    e.delete(0, END)


def button_multiply():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)


def button_divide():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0, END)


def button_modulo():
    first_num = e.get()
    global f_num
    global math
    math = "modulo"
    f_num = int(first_num)
    e.delete(0, END)


def button_power():
    first_num = e.get()
    global f_num
    global math
    math = "power"
    f_num = int(first_num)
    e.delete(0, END)


def button_equal():
    answer = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(answer))
    elif math == "subtraction":
        e.insert(0, f_num - int(answer))
    elif math == "multiplication":
        e.insert(0, f_num * int(answer))
    elif math == "division":
        e.insert(0, f_num / int(answer))
    elif math == "modulo":
        e.insert(0, f_num % int(answer))
    elif math == "power":
        e.insert(0, f_num ** int(answer))


# Defining a button
button_1 = Button(calc, text="1", padx=40, pady=20, bg="#f5f5f5", command=lambda: button_click(1))
button_2 = Button(calc, text="2", padx=40, pady=20, bg="#f5f5f5", command=lambda: button_click(2))
button_3 = Button(calc, text="3", padx=40, pady=20, bg="#f5f5f5", command=lambda: button_click(3))
button_4 = Button(calc, text="4", padx=40, pady=20, bg="#f5f5f5", command=lambda: button_click(4))
button_5 = Button(calc, text="5", padx=40, pady=20, bg="#f5f5f5", command=lambda: button_click(5))
button_6 = Button(calc, text="6", padx=40, pady=20, bg="#f5f5f5", command=lambda: button_click(6))
button_7 = Button(calc, text="7", padx=40, pady=20, bg="#f5f5f5", command=lambda: button_click(7))
button_8 = Button(calc, text="8", padx=40, pady=20, bg="#f5f5f5", command=lambda: button_click(8))
button_9 = Button(calc, text="9", padx=40, pady=20, bg="#f5f5f5", command=lambda: button_click(9))
button_0 = Button(calc, text="0", padx=40, pady=20, bg="#f5f5f5", command=lambda: button_click(0))
button_add = Button(calc, text="+", padx=40, pady=20, bg="#d4d4d4", command=button_add)
button_subtract = Button(calc, text="-", padx=42, pady=20, bg="#d4d4d4", command=button_subtract)
button_multiply = Button(calc, text="*", padx=41, pady=20, bg="#d4d4d4", command=button_multiply)
button_divide = Button(calc, text="/", padx=43, pady=20, bg="#d4d4d4", command=button_divide)
button_modulo = Button(calc, text="MOD", padx=26, pady=20, bg="#d4d4d4", command=button_modulo)
button_power = Button(calc, text="^", padx=40, pady=20, bg="#d4d4d4", command=button_power)
button_equal = Button(calc, text="=", padx=39, pady=20, bg="#99badd", command=button_equal)
button_clear = Button(calc, text="C", padx=38, pady=20, bg="#a32638", command=button_clear)

# Putting buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_subtract.grid(row=4, column=2)
button_0.grid(row=4, column=1)
button_add.grid(row=4, column=0)

button_power.grid(row=5, column=2)
button_divide.grid(row=5, column=1)
button_multiply.grid(row=5, column=0)

button_equal.grid(row=6, column=2)
button_modulo.grid(row=6, column=1)
button_clear.grid(row=6, column=0)

calc.mainloop()