import turtle
import time
import tkinter

joe = turtle.Turtle()

joe.pensize(1)
joe.shape('turtle')
joe.speed(400)

a = [1]
step = 11

for i in range(step):
    neg_a = [-x for x in a]
    neg_a.reverse()
    a.append(1)

    a += neg_a


print(a)

def heighway(a,len):
    for i in a:
        if i == 1:joe.right(90), joe.forward(len)
        if i == -1: joe.left(90), joe.forward(len)


heighway(a,5)
tkinter.mainloop()
