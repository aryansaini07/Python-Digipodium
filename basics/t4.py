from turtle import *

speed('slowest')
pencolor('blue')
sides = 25
for i in range(sides):
    forward(75)
    left(360/sides)
    dot(50)
mainloop()