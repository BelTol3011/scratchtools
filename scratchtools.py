WIDTH = 600
HEIGHT = 600
from tkinter import *
root = Tk()
canvas = Canvas(master=root, highlightthickness=0)
canvas.place(x=0, y=0, width=WIDTH, height=HEIGHT)
root.resizable(0, 0)
"""Functions"""


def size(width, height):
    global WIDTH
    global HEIGHT
    root.geometry(str(width) + "x" + str(height))
    canvas.pack_forget()
    canvas.place(x=0, y=0, width=width, height=height)
    WIDTH = width
    HEIGHT = height
    # print("geometry is now:", HEIGHT, WIDTH)


def background(color):
    color = mIntToColor(color)
    canvas.configure(bg=color )


def sleep(seconds):
    time.sleep(seconds)


def title(title):
    root.title(title)


def update():
    root.update()


def translate(x, y):
    global null
    null = (x, y)
    # print("null is now:", x, y)


def cText(x, y, text, font):
    global elements
    try:
        num = canvas.create_text(null[0] + x, null[1] + y, text=text, font=font)
        elements.append(num)
        return num
    except TclError:
        exit()


def dObject(number):
    try:
        return canvas.delete(number)
    except TclError:
        exit()

def noWindow():
    global root
    global nowin
    nowin=1
    root.destroy()


def mIntToColor(int):
    try:
        # print(int)
        usless = int + " "

        return int
    except TypeError:
        if len(str(int)) == 1:
            int = str(int) + "0"
        int = "#" + str(int) + str(int) + str(int)
        # print(int)
        return int


def Circle(x, y, dx, dy, fill=None):
    try:

        fill = mIntToColor(fill)
        #print(fill)
        if fill == "#NoneNoneNone":
            num = canvas.create_oval(null[0] + x, null[1] + y, null[0] + dx, null[1] + dy)
        else:
            num = canvas.create_oval(null[0] + x, null[1] + y, null[0] + dx, null[1] + dy, fill=fill)

        return num

    except TclError:
        exit()


def Point(x, y, fill=None):
    try:

        fill = mIntToColor(fill)
        #print(fill)
        if fill == "#NoneNoneNone":
            num = canvas.create_oval(null[0] + x, null[1] + y, null[0] + x, null[1] + y,)
        else:
            num = canvas.create_oval(null[0] + x, null[1] + y, null[0] + x, null[1] + y, fill=fill)

        return num

    except TclError:
        exit()




def Line(x, y, dx, dy, fill=None):
    try:
        if fill != None:
            fill = mIntToColor(fill)
        return canvas.create_line(null[0] + x, null[1] + y, null[0] + dx, null[1] + dy, fill=fill)
    except TclError:
        exit()

def Rectangle(x,y, dx, dy):
    #cLine(x, y, dx, y)
    #cLine(x, y, x, dy)
    #cLine(dx, y, dx, dy)
    #cLine(x, dy, dx, dy)
    return canvas.create_rectangle(null[0] + x, null[1] + y, null[0] + dx, null[1] + dy)



def windowdestroyd():
    global nowin
    try:
        return nowin
    except NameError:
        return 0


def randomint(firstvalue, secondvalue):
    return random.choice(range(firstvalue, secondvalue))


def randomchoice(list):
    return random.choice(list)


def map(fst, snd, trd, fth):
    return None
    # TODO: End this function


"""Rest"""

import random
import time


import my_scratch

null = [0, 0]

root.geometry("600x600")

try:
    my_scratch.setup()
except AttributeError:
    print("No setup")

try:
    while 1:
        my_scratch.draw()
        if windowdestroyd() == 0:

            try:
                root.update()
                pass
            except TclError:
                # print("TCL error")
                break
            #for element in elements:
                #dObject(element)
                #print(len(elements))
except AttributeError:
    print("No draw")
