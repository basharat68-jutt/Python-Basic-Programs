"""Q7-coffee customization:customize a coffe order:"small","medium", 
or "large" with an option for "extra shot" of espresso"""

order = "medium"
extra_short = True

if extra_short:
    coffe = order + " coffe with an extra shot"
else:
    coffe = order + "coffee"

print("order : " , coffe)
