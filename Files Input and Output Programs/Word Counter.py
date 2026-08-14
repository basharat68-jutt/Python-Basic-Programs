def counter():
    count = 0
    with open("Enter your txt file name here","r") as f:
        data = f.read()
        numbers = data.split()
        for i in numbers:
            count +=1
    print(count)
counter()