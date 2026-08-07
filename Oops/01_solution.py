"""Q1-Basic Class and Object = create a class car with attributes like brand and model.
Then create an instance of this class."""

class Data:
    def __init__(self,Name,Last_name):
        self.Name = Name
        self.Last_name = Last_name
data = Data("Ali","Jutt")
print(data.Name)
print(data.Last_name)
baja = Data("Anas","Hassan")
print(baja.Name)
print(baja.Last_name)


