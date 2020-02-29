#Created by Kamil Krawczyk
#02/29/2020

#Problem 6
#This program creates the shape that was requested for this activity
#I was unable to figure out how to perfectly recreate the shape displayed

import turtle

def drawShape(t):
  for i in range(5):
    t.forward(120)
    t.left(72)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("pink")

for n in range(60, 670, 60):
  drawShape(alex)

  alex.penup()
  alex.goto(0,0)
  alex.left(32)
  alex.pendown()
  

wn.exitonclick()


