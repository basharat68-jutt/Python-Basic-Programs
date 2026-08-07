"""Q6-Class Variables:Add a class variables to car that keeps track of the number 
of cars created."""

class Car:

    total_car = 0

    def __init__(self, brand,model): #__init__ is a constructer therefore we cannot change its name
        self.__brand = brand #__ start mein lgaany sy attribute private ho jata hai
        self.model = model
        Car.total_car += 1

    def chai_brand(self): #mathod bnaa k access kr skty hain
        return self.__brand + " olala"

    def full_name(self):
        return f"{self.__brand} {self.model}" #use functionallity here
    
    def fuel_type(self):
        return "petrol and diesel"
    
class ElectricCar(Car):
    def __init__ (self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"



safari = ElectricCar("Tesla","Model S","85kwh")
print(safari.fuel_type())
car = Car("Tesla","Model S") #polymorphism same mathod but different values
print(car.fuel_type())
print(Car.total_car)

# 6-Class Variables:Add a class variables to car that keeps 
# track of the number of cars created.

class Jutt:
    total_car = 0
    def __init__(self,Name,Last_Name):
        self.name = Name
        self.last_name = Last_Name
        Jutt.total_car += 1
bj = Jutt("ll","jj")
print(bj.name)
print(Jutt.total_car)
