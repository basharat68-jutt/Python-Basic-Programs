"""Q8-Function with **kargs = Create a function that accepts any number 
of keyword arguments and prints them in the format key:value."""

def delete(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


delete(name = "Chai",Jutt = "Brand")
