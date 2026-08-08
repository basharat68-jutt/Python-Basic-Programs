"""Problem 1:Timing Function Execution:write a decorator that measures the time 
a function takes to executeProblem 1:Timing Function Execution:write a 
decorator that measures the time a function takes to execute"""

import time

def timer(func):
    def wrapper(*args,**kwargs ):
        start = time.time()
        result = func(*args ,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

#agr decorator bnana hai to function k ander function bnana hoga

@timer #jb bhi is example_funtion ko call krein gy to to ye timer(timer k ilawa koe or name bhi rkh skty hain) function sy ho k he guzry ga
def example_function(n):
    time.sleep(n)

example_function(4) #ye parameter(2) phly timer function mein jaye ga