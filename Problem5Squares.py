#Created by Kamil Krawczyk
#02/29/2020

#Problem 5
#This program takes the starter code provided and creates the picture that was requested.

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
      t.forward(sz)
      t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

new_position= -5

for n in range(10, 60, 10):

  drawSquare(alex, n)

  alex.penup()
  alex.goto(new_position, new_position)
  alex.pendown()
  new_position = new_position -5

wn.exitonclick()

#import turtle
#def drawSquare(t, sz):
#   """Get turtle t to draw a square of sz side"""
#   for i in range(4):
#       t.forward(sz)
#        t.left(90)
        
#wn = turtle.Screen()

#alex = turtle.Turtle()
#alex.color("blue")

#size = [20, 40, 60, 80, 100]

#for x in size:
#    drawSquare(alex,x)
#    alex.penup()
#    alex.backward(10)       # move alex to the starting position for the next square
#    alex.right(90)
#    alex.forward(10)
#    alex.left(90)
#    alex.pendown()

#wn.exitonclick()

