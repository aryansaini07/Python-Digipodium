from turtle import *
speed(0)
i = 5
while True:
    pencolor('red')
    circle(i,i)
    left(60)
    i += 5
    if i> 1000:
        break