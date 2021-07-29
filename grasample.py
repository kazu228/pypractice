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

def move_ball(e):
    
    if e.keysym == "Right":
        ball["x"] += ball["dirx"]

    if e.keysym == "Left":
        ball["x"] -= ball["diry"]

def main():
    draw_ball()
    win.bind("<KeyPress>", move_ball)
    win.after(50, main)

main()
win.mainloop()
