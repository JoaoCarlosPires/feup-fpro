import turtle

window = turtle.Screen()
alex_the_lion = turtle.Turtle()
alex_the_lion.pensize(2)
alex_the_lion.shape("turtle")
alex_the_lion.color("blue")
window.bgcolor("green")

for i in range(12):
    alex_the_lion.penup()
    alex_the_lion.forward(100)
    alex_the_lion.pendown()
    alex_the_lion.forward(20)
    alex_the_lion.penup()
    alex_the_lion.forward(20)
    alex_the_lion.stamp()
    alex_the_lion.goto(0,0)
    alex_the_lion.left(30)
    
window.exitonclick()