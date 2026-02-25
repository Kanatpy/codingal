from numpy import *
def sq(num):
    return float(num) ** 0.5
list_input = list(input("enter a list with 4 numbers with no spaces or commas: "))
sqrtlist = []
list1 = list(map(sq,list_input))


sqrtlist.append(list1)
print( sqrtlist)