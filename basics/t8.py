from turtle import *

side = 6
shapesize(10,10)
for i in range(1,100):
    dot(100,'red')
    fd(100)
    pensize(side*i)
    lt(360/side)
    dot(90,'red')
    circle(90,180)
mainloop()