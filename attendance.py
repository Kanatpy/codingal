x = input("did you have a medical cause yes or no:")
if x == "yes":
    print("you are alowwed")
else:
    y = int(input("enter the attendance of the student:"))
    if y >=75:
        print("you are allowed")
    else:
        print("NOT allowed")