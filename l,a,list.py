list1 = [4,5,1,6,7,4,6,4,4,3,7,"kanat"]
count =0 
for i in list1:
    count+=i
avg = count/len(list1)
print(count)
print(avg)

print(min(list1))
print(max(list1))
list1.sort()
print("s =",list1[0])
print("l =",list1[-1])