# Created by Kamil Krawczyk
# 02/29/2020

# Problem 3
# This problem uses a function to multiple a list of numbers

def multiply_list(num): #function to multiple the list of numbers
  total = 1
  for x in num:
    total *= x
  return total

print(multiply_list((5, 2, 7, -1))) #output and the list of numbers