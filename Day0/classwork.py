from turtle import *
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(75)

#door
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(50)
right(90)
forward(120)
end_fill()

#roof
penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
exitonclick()