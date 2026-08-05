"""Q1-Couting positive Numbers : Given a list of numbers,count how many are positive
numbers = [1,-2,3,-4,5,6,-7,-8,9,10]"""

numbers = [1,-2,3,-4,5,-6,7,-8,9,10]
possitive_number_count = 0
for num in numbers:
    if num>0:
        possitive_number_count +=1

print("final count of possitive number is", possitive_number_count) 
