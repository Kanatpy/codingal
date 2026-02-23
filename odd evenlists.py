list1 = []
num1,num2 = int(input("enter num1: ")),int(input("enter num2: "))

num = num1 + 1
layer =1
while num <= num2:
    list1.insert(layer,num)

    layer +=1
    num+=1

odd_list = [x for x in list1 if x%2!=0]
even_list =[y for y in list1 if y%2==0]
print("evens:",even_list)
print("odds:",odd_list)
