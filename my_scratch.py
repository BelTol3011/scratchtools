from scratchtools import *

STARTPOSX = randomint(-600, 0)
STARTPOSY = randomint(-600, 0)

ENDPOSX = randomint(0, 600)
ENDPOSY = randomint(0, 600)

aktuellx = STARTPOSX
aktuelly = STARTPOSY

lastx = STARTPOSX
lasty = STARTPOSY

many = 10

listpointsx = []

listpointsy = []

CHANGE = 300

oldx = 0


points = [(1, 1)]


def setup():
    # background(51)
    # translate(WIDTH/2, HEIGHT/2)
    aktuellx = -600
    aktuelly = 0


def draw():
    global STARTPOSX, STARTPOSY, ENDPOSY, ENDPOSX, points, oldx, oldy

    for i in points:
        newx = i[0]
        newy = i[1]

        Line(oldx, oldy, newx, newy)

        oldx = newx
        oldy = newy

    if (aktuellx == ENDPOSX) and (aktuelly == ENDPOSY):
        end()
        # end()


def end():
    while 1:
        update()
