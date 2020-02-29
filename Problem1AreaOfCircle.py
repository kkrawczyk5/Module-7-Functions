# Created by Kamil Krawczyk
# 02/29/2020

# Problem 1
# This problem uses a function to calculate the area of a circle and returns the radius

import math #import math library

def areaOfCircle(r):  #function to calculate the area
  y = r**2 * math.pi
  return y

print (areaOfCircle(5)) #prints the result
