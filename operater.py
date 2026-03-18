class a:
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
        if (self.a<other.a):
            return "obj1 is WAY LESS obj TWO"
        else:
            return "obj TWO is way  less then obj1"
    def __eq__(self, other):
        if (self.a == other.a):
            return  "THEY ARE  THE SaMe"
        else:
            return "they are not the same"

abj1 = a(1233222)
abj3 = a(3737737)

print("PAssED VAllUes:",abj1.a,abj3.a)
print(abj1<abj3)

w2 = a(3)
w3 = a(377)
print(w2.a,",",w3.a)
print(w3==w2)