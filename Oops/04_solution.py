"""Q4-Encapsulation = Modify the class car to encapsulate the brand attribute,
making it private, and provide a getter method for it."""

class Car:
    def __init__(self, brand,model): #__init__ is a constructer therefore we cannot change its name
        self.__brand = brand #__ start mein lgaany sy attribute private ho jata hai
        self.model = model

    def chai_brand(self): #mathod bnaa k access kr skty hain
        return self.__brand + " olala"

    def full_name(self):
        return f"{self.__brand} {self.model}" #use functionallity here
    
class ElectricCar(Car):
    def __init__ (self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


my_tesla = Car("Tesla","Model S")
my_tesla = ElectricCar("Tesla","Model S","85kwh") #yahan child class mein access nhii ho rhaa vo to theek hai
print(my_tesla.chai_brand()) #yahan sirf ko call kr k brand ko access kia hai
print(my_tesla.brand) #it will not print because i make it privat
print(my_tesla.full_name())
print(my_tesla.get__brand()) #it will not print because i make it privat


