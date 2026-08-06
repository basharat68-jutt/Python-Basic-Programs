"""Q7-Function with *args = write a function that takes variable number of arguments 
and returns their sum"""

def chai(*args):
    for i in args:
        print(i ** 2)
    return sum(args)



print(chai(7,3,5,6,7))