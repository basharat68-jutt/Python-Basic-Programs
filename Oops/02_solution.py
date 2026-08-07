"""Q2-Class Method and Self = add a mathod to th car class that display the 
full name of the car(brand and model)."""

class Car:
    def __init__(self, brand,model): #__init__ is a constructer therefore we cannot change its name
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}" #use functionallity here
            

my_car = Car("Toyota","Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Tata","Safari")
print(my_new_car.model)
print(my_new_car.brand)