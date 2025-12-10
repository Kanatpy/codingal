print("select your ride")
print("1. bike")
print("2. car")
x = int(input("enter your choice"))

if(x ==1):
    print("what kind of bik?")
    print("1. scooty\n")
    print("2. scooter\n")
    y = int(input("enter your choice"))
    if(y ==2):
        print("you have selected scooter")
    else:
        print("you have selected scooty")
elif( x ==2):
    print("what type of car")
    print("1. sedan")
    print("2. xuv")
    z = int(input("enter your choice"))
    if(z ==2):
        print("you have selected xuv")
    else:
        print("you have selected sedan")
else:
    print("wrong choice")
