class circle:
    pi = 3.14159
    def __init__(self, radius):
        self.r = float(radius)
        
    def a(self):
        self.area = self.pi * (self.r ** 2)
        return self.area
    def p(self):
        self.curcumference = (self.r * 2) * self.pi
        return self.curcumference
radius = input("radius: ")
circ1 = circle(radius)
print(f"\n  area:{circ1.a()} , curcumference:{circ1.p()}")
