from tkinter import *
import random

win = Tk()

cv = Canvas(win, width=400, height=400)
cv.pack()

blocks = []
block_size = {"x": 75, "y": 30 }
ball = {"dirx": 15, "diry": -15, "x": 350, "y": 300, "w": 10}
bar = {"x": 0, "w": 100}
is_gameover = False
point = 0

def init_game():
    global is_gameover, point
    ball["y"] = 250
    ball["diry"] = -10
    point = 0

    for iy in range(0, 5):
        for ix in range(0, 8):
            x1 = 4 + ix * block_size["x"]
            x2 = x1 + block_size["x"]

            y1 = 4 + iy * block_size["y"]
            y2 = y1 + block_size["y"]

            color = "red"
            if (ix + iy) % 2 == 0: color = "blue"

            blocks.append([x1, y1, x2, y2, color])

def draw_objects():
    cv.delete('all')

    for w in blocks:
        x1, y1, x2, y2, c = w

        cv.create_rectangle(x1, y1, x2, y2, fill=c, width=0)

    cv.create_oval(ball["x"] - ball["w"], ball["y"] - ball["w"],
            ball["x"] + ball["w"], ball["y"] + ball["w"], fill="green")
    
    cv.create_rectangle(bar["x"], 390, bar["x"] + bar["w"], 400, fill="yellow")

def move_ball():
    global is_gameover, point

    if is_gameover:
        return
    


win.mainloop()