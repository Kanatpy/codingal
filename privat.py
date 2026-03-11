class myclass:
    __pravate = 48
    def __method(self):
        print("im inside CLASS: MYCLASS")
    def hi(self):
        print(myclass.__pravate)
        self.__method()
foo = myclass()
foo.hi()
