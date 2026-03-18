class NumConverter:
    def __init__(self):
        self.value_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

    def convert(self, num):
        if not isinstance(num, int) or not (1 <= num <= 1000):
            return f"before>{num}\nafter>not found"

        result = ""
        remaining = num
        for value, numeral in self.value_map:
            count, remaining = divmod(remaining, value)
            result += numeral * count
            if remaining == 0:
                break
        return f"before>{num}\nafter>{result}"   
x = int(input("num: "))
y=NumConverter()
print(y.convert(x))