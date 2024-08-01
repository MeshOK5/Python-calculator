from tkinter import *
from res import res
from math import sqrt


def del_zero(strin: str) -> str:
    if strin[len(strin) - 1:len(strin):] == '0':
        return strin[0:len(strin) - 2:]
    else:
        return strin


win = Tk()
win.title("Meshculator")
win.geometry("320x700")
win.resizable(False, False)

icon = PhotoImage(file="sources\icon.png")
win.iconphoto(False, icon)

label = Label(win, text="Meshculator", font=('Times', 24))
label.pack()

button_1 = Button()
button_2 = Button()
button_3 = Button()
button_4 = Button()
button_5 = Button()
button_7 = Button()
button_6 = Button()
button_8 = Button()
button_9 = Button()

buttons_array = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]

result = Label(win, font=('Times', 24))

a = False


def button_func1():
    global result, a
    if a == True and res.whatRes == True or res.result == "0" or res.result2 == "0":
        res.result = ""
        res.result2 = ""
        a = False
    if res.whatRes:
        res.result += "1"
        result.config(text=res.result)
    else:
        res.result2 += "1"
        result.config(text=res.result2)
    result.place(relx=1, rely=1)
    result.pack()


def button_func2():
    global result, a
    if a and res.whatRes == True or res.result == "0" or res.result2 == "0":
        res.result = ""
        res.result2 = ""
        a = False
    if res.whatRes:
        res.result += "2"
        result.config(text=res.result)
    else:
        res.result2 += "2"
        result.config(text=res.result2)
    result.place(relx=1, rely=1)
    result.pack()


def button_func3():
    global result, a
    if a and res.whatRes == True or res.result == "0" or res.result2 == "0":
        res.result = ""
        res.result2 = ""
        a = False
    if res.whatRes:
        res.result += "3"
        result.config(text=res.result)
    else:
        res.result2 += "3"
        result.config(text=res.result2)
    result.place(relx=1, rely=1)
    result.pack()


def button_func4():
    global result, a
    if a and res.whatRes == True or res.result == "0" or res.result2 == "0":
        res.result = ""
        res.result2 = ""
        a = False
    if res.whatRes:
        res.result += "4"
        result.config(text=res.result)
    else:
        res.result2 += "4"
        result.config(text=res.result2)
    result.place(relx=1, rely=1)
    result.pack()


def button_func5():
    global result, a
    if a and res.whatRes == True or res.result == "0" or res.result2 == "0":
        res.result = ""
        res.result2 = ""
        a = False
    if res.whatRes:
        res.result += "5"
        result.config(text=res.result)
    else:
        res.result2 += "5"
        result.config(text=res.result2)
    result.place(relx=1, rely=1)
    result.pack()


def button_func6():
    global result, a
    if a and res.whatRes == True or res.result == "0" or res.result2 == "0":
        res.result = ""
        res.result2 = ""
        a = False
    if res.whatRes:
        res.result += "6"
        result.config(text=res.result)
    else:
        res.result2 += "6"
        result.config(text=res.result2)
    result.place(relx=1, rely=1)
    result.pack()


def button_func7():
    global result, a
    if a and res.whatRes == True or res.result == "0" or res.result2 == "0":
        res.result = ""
        res.result2 = ""
        a = False
    if res.whatRes:
        res.result += "7"
        result.config(text=res.result)
    else:
        res.result2 += "7"
        result.config(text=res.result2)
    result.place(relx=1, rely=1)
    result.pack()


def button_func8():
    global result, a
    if a and res.whatRes == True or res.result == "0" or res.result2 == "0":
        res.result = ""
        res.result2 = ""
        a = False
    if res.whatRes:
        res.result += "8"
        result.config(text=res.result)
    else:
        res.result2 += "8"
        result.config(text=res.result2)
    result.place(relx=1, rely=1)
    result.pack()


def button_func9():
    global result, a
    if a and res.whatRes == True or res.result == "0" or res.result2 == "0":
        res.result = ""
        res.result2 = ""
        a = False
    if res.whatRes:
        res.result += "9"
        result.config(text=res.result)
    else:
        res.result2 += "9"
        result.config(text=res.result2)
    result.place(relx=1, rely=1)
    result.pack()


def button_func0():
    global result, a
    if a and res.whatRes == True or res.result == "0" or res.result2 == "0":
        res.result = ""
        res.result2 = ""
        a = False
    if res.whatRes:
        res.result += "0"
        result.config(text=res.result)
    else:
        res.result2 += "0"
        result.config(text=res.result2)
    result.place(relx=1, rely=1)
    result.pack()


def button_minus():
    if res.result != "" and res.typeRes == "":
        result.config(text="")
    elif res.result != "" and res.typeRes != "":
        typeRes()
    res.whatRes = False
    res.typeRes = "-"


def button_plus():
    if res.result != "" and res.typeRes == "":
        result.config(text="")
    elif res.result != "" and res.typeRes != "":
        typeRes()
    res.whatRes = False
    res.typeRes = "+"


def button_multiply():
    if res.result != "" and res.typeRes == "":
        result.config(text="")
    elif res.result != "" and res.typeRes != "":
        typeRes()
    res.whatRes = False
    res.typeRes = "*"


def button_divide():
    if res.result != "" and res.typeRes == "":
        result.config(text="")
    elif res.result != "" and res.typeRes != "":
        typeRes()
    res.whatRes = False
    res.typeRes = "/"


def degree():
    if res.result != "" and res.typeRes == "":
        result.config(text="")
    elif res.result != "" and res.typeRes != "":
        typeRes()
    res.whatRes = False
    res.typeRes = "^"


def radical():
    if res.result != "" and res.typeRes == "":
        result.config(text="")
    elif res.result != "" and res.typeRes != "":
        typeRes()
    res.typeRes = "√"
    typeRes()


def percent():
    if res.result != "" and res.typeRes == "":
        result.config(text="")
    elif res.result != "" and res.typeRes != "":
        typeRes()
    res.typeRes = "%"
    typeRes()


def erase():
    res.result = ""
    res.result2 = ""
    res.whatRes = True
    result.config(text="")


def more():
    win.geometry("600x700")

def dot():
    global result, a
    if a and res.whatRes == True or res.result == "0" or res.result2 == "0":
        res.result = ""
        res.result2 = ""
        a = False
    if res.whatRes:
        res.result += "."
        result.config(text=res.result)
    else:
        res.result2 += "."
        result.config(text=res.result2)
    result.place(relx=1, rely=1)
    result.pack()

def typeRes():
    global result
    try:
        if res.typeRes == '+':
            result.config(text=del_zero(str(float(res.result) + float(res.result2))))
            res.result = del_zero(str(float(res.result) + float(res.result2)))
        elif res.typeRes == '-':
            result.config(text=del_zero(str(float(res.result) - float(res.result2))))
            res.result = del_zero(str(float(res.result) - float(res.result2)))
        elif res.typeRes == "*":
            result.config(text=del_zero(str(float(res.result) * float(res.result2))))
            res.result = del_zero(str(float(res.result) * float(res.result2)))
        elif res.typeRes == '/':
            result.config(text=del_zero(str(float(res.result) / float(res.result2))))
            res.result = del_zero(str(float(res.result) / float(res.result2)))
        elif res.typeRes == '^':
            result.config(text=del_zero(str(float(res.result) ** float(res.result2))))
            res.result = del_zero(str(float(res.result) ** float(res.result2)))
        elif res.typeRes == '√':
            result.config(text=del_zero(str(sqrt(float(res.result)))))
            res.result = del_zero(str(sqrt(float(res.result))))
        elif res.typeRes == '%':
            result.config(text=del_zero(str(float(res.result) * 100)))
            res.result = del_zero(str(float(res.result) * 100))
        res.result2 = ""
        res.typeRes = ""
        global a
        a = True
        res.whatRes = True
        res.result2 = ""
    except:
        None


def button_equals():
    typeRes()


buttons_array[0] = Button(font=('Times', 24), command=button_func1)
buttons_array[0].pack()
buttons_array[1] = Button(font=('Times', 24), command=button_func2)
buttons_array[1].pack()
buttons_array[2] = Button(font=('Times', 24), command=button_func3)
buttons_array[2].pack()
buttons_array[3] = Button(font=('Times', 24), command=button_func4)
buttons_array[3].pack()
buttons_array[4] = Button(font=('Times', 24), command=button_func5)
buttons_array[4].pack()
buttons_array[5] = Button(font=('Times', 24), command=button_func6)
buttons_array[5].pack()
buttons_array[6] = Button(font=('Times', 24), command=button_func7)
buttons_array[6].pack()
buttons_array[7] = Button(font=('Times', 24), command=button_func8)
buttons_array[7].pack()
buttons_array[8] = Button(font=('Times', 24), command=button_func9)
buttons_array[8].pack()
button_0 = Button(text="0", font=('Times', 24), command=button_func0)
button_0.pack()

text = 1

for i in range(3):
    for r in range(3):
        buttons_array[text - 1].config(text=f"{text}")
        buttons_array[text - 1].place(x=100 * (r + 0.4), y=100 * (i + 1))
        buttons_array[text - 1].config(background="cyan3")
        text += 1

button_0.place(x=100 * 1.4, y=400)
button_0.config(background="cyan3")

button_plus = Button(text="+", font=('Times', 24), command=button_plus, background="cyan3")
button_plus.place(x=100 * 0.4, y=400)

button_minus = Button(text="-", font=('Times', 24), command=button_minus, background="cyan3")
button_minus.place(x=100 * 2.4, y=400)

button_multiply = Button(text="*", font=('Times', 24), command=button_multiply, background="cyan3")
button_multiply.place(x=100 * 0.4, y=470)

button_divide = Button(text="/", font=('Times', 24), command=button_divide, background="cyan3")
button_divide.place(x=100 * 2.4, y=470)

erase = Button(text="C", font=('Times', 24), command=erase, background="cyan3")
erase.place(x=100 * 1.4, y=470)

button_equals = Button(text="=", font=('Times', 24), command=button_equals, width=13, background="OrangeRed2")
button_equals.place(x=100 * 0.4, y=540)

more = Button(text="MORE", font=('Times', 24), command=more, width=13, background="cyan3")
more.place(x=100 * 0.4, y=600)

degree = Button(text="^", font=('Times', 24), command=degree, background="cyan3")
degree.place(x=100 * 3.4, y=100)

radical = Button(text="√", font=('Times', 24), command=radical, background="cyan3")
radical.place(x=100 * 4.4, y=100)

percent = Button(text="%", font=('Times', 24), command=percent, background="cyan3")
percent.place(x=100 * 5.4, y=100)

dot = Button(text=".", font=('Times', 24), command=dot, background="cyan3")
dot.place(x=100 * 3.4, y=200)

win.mainloop()
