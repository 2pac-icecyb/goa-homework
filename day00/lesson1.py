from turtle import *


#we want to paint a house

#step 1: draw a square
speed(30)
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square


#drawing a door

forward(70)
color("black")
begin_fill()
left(90)

forward(120) #height of the door
right(90)

forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown()

color("green")
begin_fill()

right(150)
forward(200)

left(120)
forward(200)

end_fill()

penup()
goto(30,140)
pendown()
color("silver")
begin_fill()

left(120)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)


penup()
goto(135,140)
pendown()

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

end_fill()


exitonclick()