import turtle
import time
import tkinter

def heighway(step, len):
    joe = turtle.Turtle()
    joe.pensize(1)
    joe.shape('turtle')
    joe.speed(400)

    a = [1]
    for i in range(step):
        addon = [-x for x in a]
        addon.reverse()
        addon = [1] + addon
        for i in addon:
            joe.right(90*i), joe.forward(6)
        a += addon

heighway(step=8,len=10)
tkinter.mainloop()
