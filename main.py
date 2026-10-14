import turtle
screen = turtle.Screen()
screen.bgcolor("brown")

person = turtle.Turtle()
person.shape("turtle")
person.color("orange")

def up():
    person.sety(person.ycor() + 20)

def down():
    person.sety(person.ycor() - 20)

def left():
    person.setx(person.xcor() - 20)

def right():
    person.setx(person.xcor() + 20)

screen.listen()

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

turtle.done()