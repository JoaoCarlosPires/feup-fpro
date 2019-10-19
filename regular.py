#Inicialização

import turtle

window = turtle.Screen()
alex_the_lion = turtle.Turtle()
alex_the_lion.pensize(3)

#Registo do número de lados do polígono e do comprimento de cada um

number_sides = int(input("What is the number of sides of your polygon? "))
lenght_sides = int(input("What is the lenght of each side of your polygon? "))

#Registo das cores do polígono e das bordas

border_color = str(input("What is the color of the border of your polygon? "))
alex_the_lion.color(border_color)
polygon_color = str(input("What is the color of your polygon? "))

#Cálculo da amplitude dos ângulos internos do polígono

angle = float(180 - ((number_sides-2)*(180/number_sides)))

alex_the_lion.fillcolor(polygon_color)
alex_the_lion.begin_fill()

for i in range(1, number_sides + 1):
    alex_the_lion.forward(lenght_sides)
    alex_the_lion.left(angle)

alex_the_lion.end_fill()
window.exitonclick()