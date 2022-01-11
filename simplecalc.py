import tkinter as tk
from tkinter import *
from tkinter import messagebox as m_box

window = tk.Tk()
window.title('Calculator')
window.geometry("300x400")
window.resizable(0, 0)
window.maxsize(width=300, height=600)
window.configure(background="black")

# *********************************************Functionality *********************************

val = ""
A = 0
operator = ""


def btn0_is_clicked():
    global val
    val = val + "0"
    data.set(val)


def btn1_is_clicked():
    global val
    val = val + "1"
    data.set(val)


def btn2_is_clicked():
    global val
    val = val + "2"
    data.set(val)


def btn3_is_clicked():
    global val
    val = val + "3"
    data.set(val)


def btn4_is_clicked():
    global val
    val = val + "4"
    data.set(val)


def btn5_is_clicked():
    global val
    val = val + "5"
    data.set(val)


def btn6_is_clicked():
    global val
    val = val + "6"
    data.set(val)


def btn7_is_clicked():
    global val
    val = val + "7"
    data.set(val)


def btn8_is_clicked():
    global val
    val = val + "8"
    data.set(val)


def btn9_is_clicked():
    global val
    val = val + "9"
    data.set(val)


def plus():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)


def sub():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)


def mul():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)


def div():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)


def clear():
    global val
    global A
    global operator
    A = 0
    operator = ""
    val = ""
    data.set(val)


def result():
    global A
    global operator
    global val
    if operator == "+":
        x = int((val.split("+")[1]))
        add = A + x
        data.set(add)
        val = str(add)
    elif operator == "-":
        x = int((val.split("-")[1]))
        sub= A - x
        data.set(sub)
        val = str(sub)
    elif operator == "*":
        x = int((val.split("*")[1]))
        mul = A * x
        data.set(mul)
        val = str(mul)
    elif operator == "/":
        x = int((val.split("/")[1]))
        if x == 0:
            m_box.showerror("Error", "Zero Division Error")
            A = 0
            operator = ""
            val = ""
            data.set(val)
        else:
            div = A / x
            data.set(div)
            val = str(div)


# ****************************************** End Functionality *******************************

# ******************************************* Label **************************************
data = tk.StringVar()
label1 = tk.Label(window, text="Label", font=('verdana', 14), bg="black", fg="white", textvariable=data)
label1.pack(expand=True, side='top', anchor='se')
# ******************************************* End Label **********************************

# ******************************************* Button Row 1 **********************************************
btnrow1 = tk.LabelFrame(window)
btnrow1.pack(expand=True, fill='both')
btnrow1.config(border=0, relief=GROOVE)

btn1 = tk.Button(btnrow1, text="1", border=0, relief=GROOVE, font=("verdana", 14), bg="#089696",
                 command=btn1_is_clicked)
btn1.pack(expand=True, fill='both', side='left')

btn2 = tk.Button(btnrow1, text="2", border=0, relief=GROOVE, font=("verdana", 14), bg="#089696",
                 command=btn2_is_clicked)
btn2.pack(expand=True, fill='both', side='left')

btn3 = tk.Button(btnrow1, text="3", border=0, relief=GROOVE, font=("verdana", 14), bg="#089696",
                 command=btn3_is_clicked)
btn3.pack(expand=True, fill='both', side='left')

btnadd = tk.Button(btnrow1, text="+", border=0, relief=GROOVE, font=("verdana", 14), bg="#089696", command=plus)
btnadd.pack(expand=True, fill='both', side='left')

# ******************************************* End Button Row 1 ******************************************

# ******************************************* Button Row 2 **********************************************
btnrow2 = tk.LabelFrame(window)
btnrow2.pack(expand=True, fill='both')
btnrow2.config(border=0, relief=GROOVE)

btn4 = tk.Button(btnrow2, text="4", border=0, relief=GROOVE, font=("verdana", 14), bg="#089696",
                 command=btn4_is_clicked)
btn4.pack(expand=True, fill='both', side='left')

btn5 = tk.Button(btnrow2, text="5", border=0, relief=GROOVE, font=("verdana", 14), bg="#089696",
                 command=btn5_is_clicked)
btn5.pack(expand=True, fill='both', side='left')

btn6 = tk.Button(btnrow2, text="6", border=0, relief=GROOVE, font=("verdana", 14), bg="#089696",
                 command=btn6_is_clicked)
btn6.pack(expand=True, fill='both', side='left')

btnsub = tk.Button(btnrow2, text="-", border=0, relief=GROOVE, font=("verdana", 14), bg="#089696", command=sub)
btnsub.pack(expand=True, fill='both', side='left')
# ******************************************* End Button Row 2 ******************************************

# ******************************************* Button Row 3 **********************************************
btnrow3 = tk.LabelFrame(window)
btnrow3.pack(expand=True, fill='both')
btnrow3.config(border=0, relief=GROOVE)

btn7 = tk.Button(btnrow3, text="7", border=0, relief=GROOVE, font=("verdana", 14), bg="#089696",
                 command=btn7_is_clicked)
btn7.pack(expand=True, fill='both', side='left')

btn8 = tk.Button(btnrow3, text="8", border=0, relief=GROOVE, font=("verdana", 14), bg="#089696",
                 command=btn8_is_clicked)
btn8.pack(expand=True, fill='both', side='left')

btn9 = tk.Button(btnrow3, text="9", border=0, relief=GROOVE, font=("verdana", 14), bg="#089696",
                 command=btn9_is_clicked)
btn9.pack(expand=True, fill='both', side='left')

btnmul = tk.Button(btnrow3, text="x", border=0, relief=GROOVE, font=("verdana", 14), bg="#089696", command=mul)
btnmul.pack(expand=True, fill='both', side='left')

# ******************************************* End Button Row 3 ******************************************

# ******************************************* Button Row 4 **********************************************
btnrow4 = tk.LabelFrame(window)
btnrow4.pack(expand=True, fill='both')
btnrow4.config(border=0, relief=GROOVE)

btnclear = tk.Button(btnrow4, text="c", border=0, relief=GROOVE, font=("verdana", 14), bg="#089696", command=clear)
btnclear.pack(expand=True, fill='both', side='left')

btn0 = tk.Button(btnrow4, text="0", border=0, relief=GROOVE, font=("verdana", 14), bg="#089696",
                 command=btn0_is_clicked)
btn0.pack(expand=True, fill='both', side='left')

btnequal = tk.Button(btnrow4, text="=", border=0, relief=GROOVE, font=("verdana", 14), bg="#089696", command=result)
btnequal.pack(expand=True, fill='both', side='left')

btndiv = tk.Button(btnrow4, text="/", border=0, relief=GROOVE, font=("verdana", 14), bg="#089696", command=div)
btndiv.pack(expand=True, fill='both', side='left')
# ******************************************* End Button Row 4 ******************************************
window.mainloop()
