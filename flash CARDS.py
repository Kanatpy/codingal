class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word +"(" +self.meaning+")"
flashes = []

print("Welcome To FlashWorld")

while  True:
    word = input("ENTER A WORD THAT U KNOW: ")
    meaning = input("WHAT IS THE MEANING OF THAT WORD: ")
    flashes.append(flashcard(word,meaning))
    option = int(input("IF YOU DARE TO GO AGAIN THEN ENETER 0 ELSE ENETER 1"))

    if option:
        break
print("YOUR KNOWLEDGE IS SHOWN DOWN BELOW vvvv")
for i  in flashes:
    print(">",i)