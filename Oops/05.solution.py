"""Q5-Polymorphism:demonstrate polymorphism by defining a method fuel_type in both
car and electricCar,but with different variables."""

class Car:
    def __init__(self, brand,model): #__init__ is a constructer therefore we cannot change its name
        self.__brand = brand #__ start mein lgaany sy attribute private ho jata hai
        self.model = model

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



my_tesla = ElectricCar("Tesla","Model S","85kwh")
print(my_tesla.fuel_type())
safari = Car("Tesla","Model S") #polymorphism same mathod but different values
print(safari.fuel_type())