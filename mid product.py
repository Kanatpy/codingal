num = int(input("Enter a num: "))
t = num
numlen = 0

while t >0:
    numlen = numlen +1
    t = int(t/10)

if numlen >= 4:
    numlen = int(numlen / 2)
    chk = 0
    while num>0:
        rem = num%10
        if chk == numlen:
            midone =  rem
        elif chk==numlen-1:
            midtwo =rem
        num = int(num/10)
        chk = chk +1
    prod = midone*midtwo
    print("\n product o f mid digits (" +str(midone)+ "*" +str(midtwo)+ ") = ",prod)
else:
    print("\nIts not a 4 or more than 4-digit number!")