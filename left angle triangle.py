x = int(input("enter the num of rows: "))
if x %2==0:
    y = int(x/2)
else:
    y = int(x/2)+1
z = y-1
for i in range(1,y+1):
    for j in range(1,z+1):
        print(end=" ")
    z = z-1
    a =1
#            if does not work replace  [for j in range(i-1)]  with  [for j in range(2*i-1)]  to get back to rormal
    for j in range(i-1):
        print(end=str(a))
        a = a+1
    print()
z =1
