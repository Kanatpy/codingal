num1 = [1,2,3]
num2 = [4,5,6]
result = map(lambda x,y: x+y,num1,num2)
print("addition of to lists")
print(list(result))
nums = [1,2,3,4,5]
def sq(n):
    return n*n
square = list(map(sq,nums))
print("square of nums in lists")
print(square)