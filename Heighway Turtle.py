import turtle
import time
import tkinter

def heighway(step, len):
    turt = turtle.Turtle()
    turt.pensize(1)
    turt.shape('turtle')
    turt.speed(400)

    a = [1]
    for i in range(step):
        addon = [-x for x in a]
        addon.reverse()
        addon = [1] + addon
        for i in addon:
            turt.right(90*i), turt.forward(6)
        a += addon

heighway(step=8,len=10)
tkinter.mainloop()
