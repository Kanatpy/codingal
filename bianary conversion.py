num = int(input("enter a num: "))
st = ""
while num >= 1:
    x =num % 2
    num = num//2
    x =str(x)
    st = x + st
    
print(st)