from turtle import *
speed('fastest')
colors = ['red','blue','orange']
s = len(colors)
for i in range(500):
        
        c = colors[i%s]
        pencolor(c)
        forward(i+6)
        left(360/s)
        for j in range(s):
            forward(200)
            left(360/s)

mainloop()