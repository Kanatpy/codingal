class bird:
    def __init__(self):
        print("bird is ready")
    def who(self):
        print("bird")
    def swim(self):
        print("swim faster")
class penguin(bird):
    def __init__(self):
        super().__init__()
        print("penguin is ready")
    def who(self):
        print("penguin")
    def run(self):
        print("faster faster!!!")
peggy = penguin()
peggy.who()
peggy.run()
peggy.swim()