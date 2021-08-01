from tkinter import *
import random

win = Tk()
cv = Canvas(win, width=600, height=400)
cv.pack()

blocks = []
block_size = {"x": 75, "y": 30}
ball = {"dirx": 15, "diry": -15, "x": 350, "y": 300, "w": 10}
is_gameover = False
point = 0


def init_game():
    global is_gameover, point

    is_gameover = False
    ball["y"] = 250
    ball["diry"] = -10
    point = 0

    for iy in range(0, 5):
        for ix in range(0, 8):
            color = "red"

            if (iy + ix) % 2 == 1: color = "blue"
            x1 = 4 + ix * block_size["x"]
            x2 = x1 + block_size["x"]

            y1 = 4 + iy * block_size["y"]
            y2 = y1 + block_size["y"]

            blocks.append([x1, y1, x2, y2, color])

    win.title('START')            


init_game()
