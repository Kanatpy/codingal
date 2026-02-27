class employee:
    def __init__(self):
        print("employee called")
    def __del__(self):
        print("destroyer CALLED")
def create_obj():
    print("making obj")
    obj =employee()
    print("func end...")
    return obj
print("calling create_obj() func...")
obj =create_obj()
print("program end...")