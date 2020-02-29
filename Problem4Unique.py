# Created by Kamil Krawczyk
# 02/29/2020

# Problem 4
# This problem uses a function look at a list of numbers and remove any repeats

def new_unique_list(num): #function to remove the repeat numbers
  list = []
  for n in num:
    if n not in list:
      list.append(n)
  return list

print (new_unique_list([1, 3, 3, 3, 6, 2, 3, 5])) #prints the list with only non-repeated numbers