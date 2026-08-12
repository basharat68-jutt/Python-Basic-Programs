def count():
    count_even = 0
    count_odd =0
    with open("enter your txt file name here","r") as f:
        data = f.read()
        numbers = data.split(",")
        for i in numbers:
            if int(i) % 2 == 0:
                count_even += 1
            elif int(i) % 2 != 0:
                count_odd += 1
    return count_even,count_odd
print(count())