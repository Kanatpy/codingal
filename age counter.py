try:
    print("what is your age: ")
    age = int(input())
    if age % 2 == 0:
        print("even age")

    else:
        print("odd")

except ValueError:
    print("wrong value")
except SyntaxError:
    print("wrong syntax")
except:
    print("wrong input")
