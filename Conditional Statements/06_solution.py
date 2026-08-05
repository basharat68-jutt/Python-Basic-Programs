"""Q6-transportation mood selection:choose a mode of transportation based 
on the distance(eg <3km:walk,3-15km:bike>15km:car)"""

distance = 12

if distance<3:
    activity = "walk"
elif distance<15:
    activity = "bike"
else:
    activity = "car"

print(activity )