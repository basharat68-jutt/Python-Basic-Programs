"""Q8-Prime Number Checker : Check if number is prime"""

number = 25
is_true = True 

if number > 1:
    for i in range(2,number):
        if (number % i) == 0:
            is_true = False
            break

print(is_true)