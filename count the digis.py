num = int(input("enter a num: "))
temp = num
count = 0
while (temp>0):
    temp = temp//10
    count += 1
print(count)