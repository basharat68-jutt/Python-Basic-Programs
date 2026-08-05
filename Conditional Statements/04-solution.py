"""Q4-fruit ripeness checker:determine if a fruit is ripe,overripe, or unique based 
on its colour.(eg Banana:Green-unique,yellow-ripe,brown-overripe)"""

fruit = "banana"
colour = "yellow"

if fruit == "banana":
    if colour == "green":
        print("unripe")
    elif colour == "yellow":
        print("ripe")
    elif colour == "brown":
        print("overripe")