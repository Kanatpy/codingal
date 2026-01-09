x = int(input("enter the num of rows: "))
z = x-1
for i in range(1,x+1):
    for j in range(1,z+1):
        print(end=" ")
    z = z-1
    a =1
#            if does not work replace  [for j in range(2*i-1)]  with  [for j in range(2*i-1)]  to get back to rormal
    for j in range(1,i+1):
        print(end="*")
        a = a+1
    print()
z =1
