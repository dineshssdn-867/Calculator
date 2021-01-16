#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from functools import lru_cache
root = Tk()

# trace of main answer

answer = 0

# trace of operation

trace = ''

# trace of count of subtraction  operation

count_sub = 0

# trace of count of multiplication operation

count_mult = 0

# trace of count of division  operation

count_div = 0

# Title of calculator app

root.title('Simple Calculator')

# creating a input parameter

e = Entry(root, width=50, borderwidth=5)

# showing it on the screen

e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# function for display

def button_click(number):

    # getting value of textbox

    current = e.get()

    # deleting old value and overwriting on it

    e.delete(0, END)

    # inserting new value to it

    e.insert(0, str(current) + str(number))


# function for clearing screen

def button_clear():

    # clearing all traces or setting it to old default value

    global answer, trace, count_sub, count_div, count_mult
    answer = 0
    trace = ''
    count_sub = 0
    count_mult = 0
    count_div = 0
    e.delete(0, END)


# function for addition

def Button_add():

    # getting value of textbox

    val = e.get()

    # deleting old value and overwriting on it

    e.delete(0, END)
    val = int(val)
    global answer, trace

    # tracing value

    trace = '+'

    # computing addition

    answer = answer + val


# function for subtraction

def button_sub():

    # getting value of textbox

    val = e.get()

    # deleting old value and overwriting on it

    e.delete(0, END)
    val = int(val)
    global answer, trace, count_sub
    trace = '-'

    # tracing values from count

    if count_sub == 0:
        answer = val - answer
        count_sub = count_sub + 1
        return

    # computing subtraction

    answer = answer - val


# Saving computation power
# function for multiplication

@lru_cache(maxsize=128, typed=False)
def button_mult():

    # getting value of textbox

    val = e.get()

    # deleting old value and overwriting on it

    e.delete(0, END)
    val = int(val)
    global answer, trace, count_mult

    # tracing values from count

    if count_mult == 0:
        answer = 1 * val
        count_mult = count_mult + 1
        trace = '*'
        return

    # computing multiplication

    answer = answer * val


# function for divison

def button_div():

    # getting value of textbox

    val = e.get()

    # deleting old value and overwriting on it

    e.delete(0, END)
    val = int(val)

    # Solving this app from exception

    if val == 0:
        e.insert(0, 'Please provide a valid input')
        return
    global answer, trace, count_div

    # tracing values from count

    if count_div == 0:
        answer = val
        count_div = count_div + 1
        trace = '/'
        return

    # computing divison

    answer = answer / val


# function for divison

def button_equal():

    # getting value of textbox

    val = e.get()
    val = int(val)
    global answer

    # deleting old value and overwriting on it

    e.delete(0, END)

    # final calcuation form traces

    if trace == '+':
        answer = answer + val
    elif trace == '-':
        answer = answer - val
    elif trace == '*':
        answer = answer * val
    elif trace == '/' and val != 0:
        answer = answer / val
    else:
        e.insert(0, 'Please provide a valid input')
        return
    e.insert(0, answer)


# definng button

Button_1 = Button(root, text='1', padx=40, pady=20, command=lambda : \
                  button_click(1))
Button_2 = Button(root, text='2', padx=40, pady=20, command=lambda : \
                  button_click(2))
Button_3 = Button(root, text='3', padx=40, pady=20, command=lambda : \
                  button_click(3))
Button_4 = Button(root, text='4', padx=40, pady=20, command=lambda : \
                  button_click(4))
Button_5 = Button(root, text='5', padx=40, pady=20, command=lambda : \
                  button_click(5))
Button_6 = Button(root, text='6', padx=40, pady=20, command=lambda : \
                  button_click(6))
Button_7 = Button(root, text='7', padx=40, pady=20, command=lambda : \
                  button_click(7))
Button_8 = Button(root, text='8', padx=40, pady=20, command=lambda : \
                  button_click(8))
Button_9 = Button(root, text='9', padx=40, pady=20, command=lambda : \
                  button_click(9))
Button_0 = Button(root, text='0', padx=40, pady=20, command=lambda : \
                  button_click(0))
button_add = Button(root, text='+', padx=40, pady=20,
                    command=Button_add)
Button_sub = Button(
    root,
    text='-',
    padx=40,
    pady=20,
    command=button_sub,
    width=1,
    )
Button_mult = Button(root, text='X', padx=40, pady=20,
                     command=button_mult)
Button_div = Button(
    root,
    text='/',
    padx=40,
    pady=20,
    command=button_div,
    width=1,
    )
Button_equal = Button(root, text='=', padx=91, pady=20,
                      command=button_equal)
Button_clear = Button(
    root,
    text='clear',
    padx=46,
    pady=20,
    command=button_clear,
    width=40,
    )

# putting on the screen

Button_1.grid(row=3, column=0)
Button_2.grid(row=3, column=1)
Button_3.grid(row=3, column=2)
Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)
Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)
Button_sub.grid(row=2, column=3)
Button_mult.grid(row=3, column=3)
Button_div.grid(row=4, column=3)
Button_0.grid(row=4, column=0)
Button_equal.grid(row=4, column=1, columnspan=2)
Button_clear.grid(row=5, column=0, columnspan=4)

# running the process

root.mainloop()
