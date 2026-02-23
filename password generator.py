import random
import string
from random_word import *


result = []
num_of_letters = random.randint(4,9)
words1 = RandomWords()
words = words1.get_random_word()
words1 = words1.get_random_word()
digits = random.choices(string.digits, k=random.randint(1,5))
symbols = random.choices(string.punctuation, k =random.randint(0,4))
result.extend(words)
result.extend(digits)
result.extend(symbols)
result.extend(words1)
random.shuffle(result)
password = ''.join(result)
print(password)