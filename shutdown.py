def shutdown():
    print("this is a shutdown function")
def restart():
    print("this is a restart function")

#main

choice = input("shutdown or restart: ")
if choice == "shutdown":
    shutdown()
else:
    restart()
