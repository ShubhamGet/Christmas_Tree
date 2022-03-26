from turtle import *

speed(0)

#Blue Background

penup()
goto(0,-250)
pendown()
color("cyan")
begin_fill()
circle(260)
end_fill()

# tree Trunk

penup()
goto(-15,-50)
pendown()
color("brown")
begin_fill()
for i in range(2):
    forward(30)
    right(90)
    forward(40)
    right(90)
end_fill()

# set the star positin and the initil tree width

y=-50
width=240
height=25

# gree section of tree

while width>20:
    width=width-30 # make the tree get smaller as it goes up in height
    x=0-width/2 # set the starting x-value of each level of the tree
    color("green")
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

    y=y+height  # keep drawing the level of the tree higher than previous

#star
penup()
goto(-15,150)
pendown()
color("yellow")
begin_fill()
for i in range(5):
    forward(30)
    right(144)
end_fill()
    
# message

penup()
goto(-200,-150)
color("yellow")
write("Merry Christmas 2021 From Shubham Singh ", font=("Arial",14,"bold"))
hideturtle()
