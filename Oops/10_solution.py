"""Q10_Multiple Inheritance:create two classes battry and engine,and let the
ElectricCar class inherit from both,drmonstrating multiple inheritance"""

class Battery:
    def battery_info(self):
        return "this is battery"
class Engine:
    def engine_info(self):
        return "ths is engine"

class Electric(Battery,Engine,Car): #Multiliple Inheritance
    pass

tesla = Electric("gg","ff")
print(tesla.model)
print(tesla.battery_info())