class computer:
    def __init__(self):
        self.__maxprice= 900
    def sell(self):
        print(f"Selling price{self.__maxprice}")
    def set_max_price(self,price):
        self.__maxprice = price
c = computer()
c.sell()

c.__maxprice = 10000
c.sell()

c.set_max_price(1000000000000000000000000)
c.sell()