try:
    num =int(input("enter a num: "))
    print("num is",num)
except ValueError as ex:
    print("exception:",ex)