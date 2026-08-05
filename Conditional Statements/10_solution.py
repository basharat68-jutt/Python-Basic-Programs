"""Q10-pet food recommendation:recommend a type of pet food based on the pets 
species and age(eg dog<2 years-puppy food,>5 years-senior cat food)"""

pet = "dog"
year = 2

if (pet=="dog" and year < 2):
    print("eat the puppy food")

else:
    print("give him adult food ")