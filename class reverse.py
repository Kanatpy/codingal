class sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.result = self.sentence.split()
        for word in self.result: 
            print(word[::-1])

a = input()
z = sentence(a)