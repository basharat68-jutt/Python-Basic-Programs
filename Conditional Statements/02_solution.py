"""Q2-movie ticket pricing:movie tickets are priced based on age:$12
for adults(18 and over),$8 for children,everyone gets a $2 discount on wednesday"""

age = 26
day = "wednesday"

price = 12 if age >= 18 else 8 

if day=="wednesday":
    price = price - 2
    # price -= 2

print("ticket price for you is $",price)