"""Q5-Find the first non-repeated character : given a string ,
find the non-repeating character"""

input_str = "teeteracdacd";

for char in input_str:
    if input_str.count(char) == 1:
        print("char is", char)