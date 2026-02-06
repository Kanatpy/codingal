def palindrome(p):
    e = len(p) -1
    s = 0
    while (s < e):
        if (p[s]!=p[e]):
            return False
        
        s+=1
        e-=1
    return True

palindrom = eval(input("enter nums seperated by commas"))

if palindrome(palindrom):
    print("palimdrome")
else:
    print("not palimdrome")