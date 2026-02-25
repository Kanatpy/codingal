class vehicle:
    def __init__(self,max_speed,milage,cost,tire_brand):
        self.max_speed = max_speed
        self.milage =milage
        self.cost =cost
        self.tirebrand=tire_brand
modley = vehicle(200,400,30000,"tires of tires")
modlex = vehicle(199,399,20000,"tired tires") 
print(f"stats of modle x: max speed: {modlex.max_speed} , milage: {modlex.milage} , cost: {modlex.cost} , tires: {modlex.tirebrand}") 
print(f"stats of modle y: max speed: {modley.max_speed} , milage: {modley.milage} , cost: {modley.cost} , tires: {modley.tirebrand}") 