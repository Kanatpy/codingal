list1 = []
list2 = []
num1,num2 = int(input("enter num1: ")),int(input("enter num2: "))

num = num1 + 1
layer =1
while num <= num2:
    if num % 2 == 0:
        list1.insert(layer,num)
    else:
        list2.insert(layer,num)

    layer +=1
    num+=1
print("evens:",list1)
print("odds:",list2)
