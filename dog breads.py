from time import sleep as wait 

class dog:
    species = "dog"
    def __init__(self, breed, age, gender):
        self.breed = breed
        self.age = age
        self.gender = gender

class cat:
    species = "cat"
    def __init__(self, breed, age, fur_pattern, gender):
        self.breed = breed
        self.age = age
        self.fur_pattern = fur_pattern
        self.gender = gender

pebbles = cat("american shorthair", 1, "tuxedo", "boy")
winnie = dog("big dog", 2, "girl")
douk = dog("bull dog", 1, "boy")

print("these are our dogs:\n")
print(f"winnie: breed:{winnie.breed} , age:{winnie.age} , gender:{winnie.gender} , species:{winnie.species}")
wait(1)
print(f"douk: breed:{douk.breed} , age:{douk.age} , gender:{douk.gender} , species:{douk.species}")
wait(1)
print(f"pebbles: breed:{pebbles.breed} , age:{pebbles.age} , gender:{pebbles.gender} , type:{pebbles.fur_pattern} , species:{pebbles.species}")
wait(0.6)
print("Hey Pebbles is not a dog!")
wait(2)
