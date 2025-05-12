from tkinter import *
window = Tk()


def button_press(num):
    global text
    text = text + str(num)
    text_label.set(text)

def equal():
    global text

    try:
        total = str(eval(text))
        text_label.set(total)
        text=total
    except SyntaxError:
        text_label.set("syntax error")
        text = ""
    except ZeroDivisionError:
        text_label.set("zerodivision error")
        text = ""


def clear():
    global text
    text_label.set("")
    text = ""
    

window.title("Calculator program")
window.geometry("500x500")


text = ""
text_label = StringVar()

label = Label(window,textvariable=text_label,width=30,height=2,bg='white',font=('arial',20))
label.pack()
frame = Frame(window)
frame.pack()

b1 = Button(frame,text=1,height=4,width=7,font=40,command=lambda:button_press(1))
b1.grid(row=0,column=0)

b2 = Button(frame,text=2,height=4,width=7,font=40,command=lambda:button_press(2))
b2.grid(row=0,column=1)

b3 = Button(frame,text=3,height=4,width=7,font=40,command=lambda:button_press(3))
b3.grid(row=0,column=2)

b4 = Button(frame,text=4,height=4,width=7,font=40,command=lambda:button_press(4))
b4.grid(row=1,column=0)

b5 = Button(frame,text=5,height=4,width=7,font=40,command=lambda:button_press(5))
b5.grid(row=1,column=1)

b6 = Button(frame,text=6,height=4,width=7,font=40,command=lambda:button_press(6))
b6.grid(row=1,column=2)

b7 = Button(frame,text=7,height=4,width=7,font=40,command=lambda:button_press(7))
b7.grid(row=2,column=0)

b8 = Button(frame,text=8,height=4,width=7,font=40,command=lambda:button_press(8))
b8.grid(row=2,column=1)

b9 = Button(frame,text=9,height=4,width=7,font=40,command=lambda:button_press(9))
b9.grid(row=2,column=2)

b0 = Button(frame,text=0,height=4,width=7,font=40,command=lambda:button_press(0))
b0.grid(row=3,column=0)


plus = Button(frame,text='+',height=4,width=7,font=40,command=lambda:button_press('+'))
plus.grid(row=0,column=3)

minus = Button(frame,text='-',height=4,width=7,font=40,command=lambda:button_press('-'))
minus.grid(row=1,column=3)

multiply = Button(frame,text='*',height=4,width=7,font=40,command=lambda:button_press('*'))
multiply.grid(row=2,column=3)

divide = Button(frame,text='/',height=4,width=7,font=40,command=lambda:button_press('/'))
divide.grid(row=3,column=3)

decimal = Button(frame,text='.',height=4,width=7,font=40,command=lambda:button_press('.'))
decimal.grid(row=3,column=1)

equal = Button(frame,text='=',height=4,width=7,font=40,command=equal)
equal.grid(row=3,column=2)

clear = Button(window,text='clear',height=4,width=7,bg='orange',font=40,command=clear)
clear.pack()


window.mainloop()
