class Parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age =age
blu = Parrot("blu",10)
woo = Parrot("woo",15)
print(f"Blu is a {blu.species}")
print(f"Woo is a {woo.species}")
print(f"{blu.name} is {blu.age} years old")
print(f"{woo.name} is {woo.age} years old")