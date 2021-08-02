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
            color = "red"

            if (iy + ix) % 2 == 1: color = "blue"
            x1 = 4 + ix * block_size["x"]
            x2 = x1 + block_size["x"]

            y1 = 4 + iy * block_size["y"]
            y2 = y1 + block_size["y"]

            blocks.append([x1, y1, x2, y2, color])

    win.title('START')            

def draw_objects():

    cv.delete('all')
    cv.create_rectangle(0, 0, 600, 400, fill="black", width=0)

    for w in blocks:
        x1, y1, x2, y2, c = w

        cv.create_rectangle(x1, y1, x2, y2, fill=c, width=0)

    cv.create_oval(ball["x"] - ball["w"], ball["y"] - ball["w"],
            ball["x"] + ball["w"], ball["y"] + ball["w"], fill="green")

    cv.create_rectangle(bar["x"], 390, bar["x"] + bar["w"], 400,
                fill="yellow")

def move_ball():
    global is_gameover, point

    if is_gameover: return

    bx = ball["x"] + ball["dirx"]
    by = ball["y"] + ball["diry"]

    if bx < 0 or bx > 600: ball["dirx"] *= -1
    if by < 0: ball["diry"] += -1

    if by > 390 and (bar["x"] <= bx <= (bar["x"] + bar["w"])):
        ball["diry"] *= -1
        if random.randint(0, 1) == 0: ball["dirx"] *= -1
        by = 380

    



init_game()
draw_objects()


win.mainloop()