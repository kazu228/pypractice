#pythonでグラフィック
from tkinter import *

ball = {
    "x": 300,
    "y": 200,
    "z": 10,
    "dirx": 15,
    "diry": 15
}

win = Tk()

cv = Canvas(win, width = 600, height = 400)
cv.pack()

def draw_ball():
    cv.delete('all')

    cv.create_oval(ball["x"] - ball["z"], ball["y"] - ball["z"],
                    ball["x"] + ball["z"], ball["y"] + ball["z"], fill="red")


def draw_line():
    x1 = 0
    x2 = 600
    y = 210
    cv.create_line(x1, y, x2, y)


def move_ball(e):
    
    if e.keysym == "Right":
        ball["x"] += ball["dirx"]

    if e.keysym == "Left":
        ball["x"] -= ball["dirx"]

    if e.keysym == "Up":
        ball["y"] -= ball["diry"]

def main():
    draw_ball()
    draw_line()
    win.bind("<KeyPress>", move_ball)
    win.after(50, main)

main()
win.mainloop()
