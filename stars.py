import turtle

window = turtle.Screen()
alex_the_lion = turtle.Turtle()
alex_the_lion.pensize(2)
alex_the_lion.shape("circle")
alex_the_lion.color("white")
window.bgcolor("blue")

number_sides = int(input("What is the number of sides of your polygon? "))
angle = float(180 - ((number_sides-2)*(180/number_sides)))

for i in range(number_sides):
    alex_the_lion.forward(100)
    alex_the_lion.stamp()
    alex_the_lion.goto(0,0)
    alex_the_lion.left(angle)
    
window.exitonclick()