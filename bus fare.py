class Vehicle:
    def __init__(self, price, seating):
        self.price = price
        self.seating = seating

class Bus(Vehicle):
    def __init__(self, price, seating):
        super().__init__(price, seating)  
        self.bus_price = self.price * 100
        self.bus_seating = self.seating * 100

    def fees(self):
        busfee = (self.bus_price / 100) * 10
        return busfee + self.bus_price 

    def display(self):
        total = self.fees()
        print(f"price before: {self.price} seating before {self.seating}\nprice now: {total} seating now: {self.bus_seating}")

bus_fare_bus = Bus(10, 10)
bus_fare_bus.display()