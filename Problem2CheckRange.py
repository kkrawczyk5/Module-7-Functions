# Created by Kamil Krawczyk
# 02/29/2020

# Problem 2
# This problem takes a number and outputs if the number is within the given range

def given_range(x): #function for the range 
  if x in range(1,10):
    print (x, "is in the range")
  else:
    print(x, "is not in the range")

given_range(5)  #number to see if it is in range

