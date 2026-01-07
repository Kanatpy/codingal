def add(p,q):
    return p+q
def subrtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
print("please select the operation")
print("a.add")
print("b.subtract")
print("c.multiply")
print("d.divide")

choice = input("please enter a choice a/b/c/d")


n1 =  int(input("what is your 1st num:"))
n2 = int(input("what is your 2st num:"))


if choice == "a":
    add(n1,n2)
elif choice == "b":
    subrtract(n1,n2)
elif choice == "c":
    multiply(n1,n2)
elif choice == "d":
    divide(n1,n2)
else:
    print("this is an invalid")