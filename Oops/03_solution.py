"""Q3-Inheritance = Create an ElectricCar class that inherits from the car class 
and has an additonal attribute."""

class Car:
    def __init__(self, brand,model): #__init__ is a constructer therefore we cannot change its name
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}" #use functionallity here
    
class ElectricCar(Car):
    def __init__ (self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla","Model S","85KWh")
print(my_tesla.model)
print(my_tesla.full_name())
