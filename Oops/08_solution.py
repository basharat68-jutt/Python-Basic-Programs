"""Q8-Property Decoraters:use a property decorator in the car class to make the model
attribute read-only.
"""

class Car:

    total_car = 0

    def __init__(self, brand,model): #__init__ is a constructer therefore we cannot change its name
        self.__brand = brand #__ start mein lgaany sy attribute private ho jata hai
        self.__model = model
        Car.total_car += 1

    def chai_brand(self): #mathod bnaa k access kr skty hain
        return self.__brand + " olala"

    def full_name(self):
        return f"{self.__brand} {self.__model}" #use functionallity here
    
    def fuel_type(self):
        return "petrol and diesel"
    

    @property #___________________________Decorator change nhii hony dy ga model s ko city mein
    def model(self):
        return self.__model
    
    @staticmethod #___________________________Decorator
    def general_description():
        return "Cars are means of transport"
    
class ElectricCar(Car):
    def __init__ (self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"



# safari = ElectricCar("Tesla","Model S","85kwh")
# print(safari.fuel_type())
ff = Car("Tesla","Model S") #polymorphism same mathod but different values
ff.model =="start"
print(ff.model)
# print(ff.fuel_type())
# print(Car.total_car)
#print(ff.general_description()) isko class access kr skti hai lekin object access nehein kr skta
