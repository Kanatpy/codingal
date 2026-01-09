def factorial(x):
    '''this is  a function  to find the factorialof an int'''
    if x ==0 or x ==1:
        return 1
    else:
        return x*factorial(x-1)
fact = int(input("enter a num from 1 to 999:"))
print(factorial.__doc__)
print("the factorial of",fact,":",factorial(fact))