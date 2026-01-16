try:
    num1, num2 = eval(input("enter two nums, seperated by comma : "))
    result = num1/num2
    print("result is",result)
except ZeroDivisionError:
    print("zero division error")
except SyntaxError:
    print("no comma. enter nums like this: 1, 2")
except:
    print("wrong input")
else:
    print("no exeptions")