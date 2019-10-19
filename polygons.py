import turtle

window = turtle.Screen()
alex_the_lion = turtle.Turtle()
alex_the_lion.pensize(3)

for i in range(4):
    alex_the_lion.color("blue")
    alex_the_lion.forward(50)
    alex_the_lion.left(90)

for i in range(3):
    alex_the_lion.color("orange")
    alex_the_lion.forward(50)
    alex_the_lion.left(120)

for i in range(6):
    alex_the_lion.color("black")
    alex_the_lion.forward(50)
    alex_the_lion.left(60)

for i in range(8):
    alex_the_lion.color("green")
    alex_the_lion.forward(50)
    alex_the_lion.left(45)

window.exitonclick()
    