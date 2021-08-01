from tkinter import *
import random

win = Tk()

cv = Canvas(win, width=600, height=400)
cv.pack()

blocks = []
block_size = {"x": 75, "y": 30}
ball = {"dirx": 15, "diry": -15, "x": 350, "y": 300, "w": 10}
bar = {"x": 0, "w": 100 }
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
            x1 = 4 + ix * block_size["x"]
            x2 = x1 + block_size["x"]

            



win.mainloop()