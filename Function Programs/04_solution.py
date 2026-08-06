"""Q4-Funtion returning multiple values = create a function that returns both
the area and circumference of a circle given its radius."""

import math
def circle_status(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area,circumference