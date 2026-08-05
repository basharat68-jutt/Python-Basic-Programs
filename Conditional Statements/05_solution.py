"""Q5-weather activity suggestion:suggest an activity based on the 
weather(eg Sunny-go for a walk,Rainy-Read a book,Snowy-build a snowman)."""

weather = "snowy"

if weather == "sunny":
    activity = "go for a walk"
elif weather == "rainy":
    activity = "read a book"
elif weather == "snowy":
    activity = "build a snowman"

print(activity)