from turtle import *

speed('fastest')
bgcolor('black')
pencolor('red')
penup()
setpos(-200,200)
pendown()
for i in range(200,0,-3):
    forward(i)
    left(90)
penup()
setpos(200,200)
pendown()
for i in range(200,0,-3):
    forward(i)
    left(90)
penup()   
setpos(+200,-200)
pendown()
for i in range(200,0,-3):
    forward(i)
    left(90)
penup() 
setpos(-200,-200)
pendown()
for i in range(200,0,-3):
    forward(i)
    left(90)
    
mainloop()