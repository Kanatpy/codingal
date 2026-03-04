class circle:
    pi = 3.14159
    def __init__(self, radius):
        r = float(radius)
        self.area = self.pi * (r ** 2)
        self.curcumference = (r * 2) * self.pi
radius = input("radius: ")
circ1 = circle(radius)
print(f"\n  area:{circ1.area} , curcumference:{circ1.curcumference}")
