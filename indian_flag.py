import turtle

def rectangle(color):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.forward(400)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()

def circle():
    t.color("blue")
    t.circle(49)
    t.up()
    t.goto(175,150)
    t.down()
    t.forward(49)
    for i in range(1,25):
        t.up()
        t.right(15)
        t.goto(175,150)
        t.down()
        t.forward(49)
    t.color("black")
    

    

t = turtle.Turtle()

t.up()
t.goto(-50, -300)
t.down()
t.goto(-50, 300)
rectangle("orange")

t.up()
t.goto(-50, 200)
t.down()
rectangle("white")
t.up()
t.goto(175, 101)
t.down()
circle()

t.up()
t.goto(-50, 100)
t.down()
rectangle("green")


#################PROGRAM WAREHOUSE###############

t.width(2.5)

#P

t.up()
t.goto(50,-200)
t.down()
t.left(90)
t.forward(50)
t.right(90)
t.forward(25)
t.right(90)
t.forward(25)
t.right(90)
t.forward(25)

#R

t.up()
t.goto(85,-200)
t.down()
t.right(90)
t.forward(50)
t.right(90)
t.forward(25)
t.right(90)
t.forward(25)
t.right(90)
t.forward(25)
t.right(215)
t.forward(35)

#O

t.up()
t.goto(120,-200)
t.down()
t.left(125)
t.forward(50)
t.right(90)
t.forward(25)
t.right(90)
t.forward(50)
t.right(90)
t.forward(25)

#G

t.up()
t.goto(155,-200)
t.down()
t.right(90)
t.forward(50)
t.right(90)
t.forward(25)
t.up()
t.goto(155,-200)
t.down()
t.forward(12.5)
t.left(90)
t.forward(12.5)
t.right(90)
t.forward(12.5)
t.right(90)
t.forward(12.5)
t.right(90)

#R

t.up()
t.goto(190,-200)
t.down()
t.right(90)
t.forward(50)
t.right(90)
t.forward(25)
t.right(90)
t.forward(25)
t.right(90)
t.forward(25)
t.right(215)
t.forward(35)

#A

t.up()
t.goto(225,-200)
t.down()
t.left(125)
t.forward(50)
t.right(90)
t.forward(25)
t.right(90)
t.forward(50)
t.up()
t.goto(225,-175)
t.down()
t.left(90)
t.forward(25)

#M

t.up()
t.goto(260,-200)
t.down()
t.left(90)
t.forward(50)
t.right(135)
t.forward(17.677669529663688110021109052621)
t.left(90)
t.forward(17.677669529663688110021109052621)
t.right(135)
t.forward(50)

#W

t.up()
t.goto(50,-280)
t.down()
t.right(180)
t.forward(50)
t.up()
t.goto(50,-280)
t.down()
t.right(45)
t.forward(17.677669529663688110021109052621)
t.right(90)
t.forward(17.677669529663688110021109052621)
t.left(135)
t.forward(50)

#A

t.up()
t.goto(85,-280)
t.down()
t.forward(50)
t.right(90)
t.forward(25)
t.right(90)
t.forward(50)
t.up()
t.goto(85,-255)
t.down()
t.left(90)
t.forward(25)

#R

t.up()
t.goto(120,-280)
t.down()
t.left(90)
t.forward(50)
t.right(90)
t.forward(25)
t.right(90)
t.forward(25)
t.right(90)
t.forward(25)
t.right(215)
t.forward(35)

#E

t.up()
t.goto(155,-280)
t.down()
t.left(125)
t.forward(50)
t.right(90)
t.forward(25)
t.up()
t.goto(155,-255)
t.down()
t.forward(15)
t.up()
t.goto(155,-280)
t.down()
t.forward(25)

#H

t.up()
t.goto(190,-280)
t.down()
t.left(90)
t.forward(50)
t.up()
t.goto(190,-255)
t.down()
t.right(90)
t.forward(25)
t.up()
t.goto(215,-280)
t.down()
t.left(90)
t.forward(50)


#O

t.up()
t.goto(225,-280)
t.down()
t.forward(50)
t.right(90)
t.forward(25)
t.right(90)
t.forward(50)
t.right(90)
t.forward(25)

#U

t.up()
t.goto(260,-280)
t.down()
t.right(90)
t.forward(50)
t.up()
t.goto(260,-280)
t.down()
t.right(90)
t.forward(25)
t.left(90)
t.forward(50)

#S

t.up()
t.goto(295,-280)
t.down()
t.right(90)
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.right(90)
t.forward(25)
t.right(90)
t.forward(25)


#E

t.up()
t.goto(330,-280)
t.down()
t.left(90)
t.forward(50)
t.right(90)
t.forward(25)
t.up()
t.goto(330,-255)
t.down()
t.forward(15)
t.up()
t.goto(330,-280)
t.down()
t.forward(25)
