import turtle
t=turtle.Pen()
t.speed(0)
t.penup()
t.setx(125)
t.sety(336)
t.right(90)
t.pendown()
t.forward(336*2)
t.penup()
t.setx(-125)
t.pendown()
t.backward(336*2)
t.penup()
t.setx(-375)
t.sety(125)
t.pendown()
t.left(90)
t.forward(375*2)
t.penup()
t.sety(-125)
t.pendown()
t.backward(375*2)
turnone = input("Which square Player1?")
if turnone == "topright":
    t.setx(-62.5)
    t.sety(62.5)
    input("hi")