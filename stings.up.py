class iostring():
    def __init__(self):
        self.str1 = ""
    def get_str(self):
        self.str1 = input("enter a str: ")
    def print_str(self):
        print("input in upercase is:",self.str1.upper())
str1 = iostring()
str1.get_str()
str1.print_str()