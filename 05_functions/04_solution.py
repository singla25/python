# Write a function that returns both the area and circumference of circle given its radius

import math

def circle(r):
    area = math.pi * (r**2)
    circumference = 2 * math.pi * r
    rounded_area = round(area, 2)
    rounded_circumference = round(circumference, 2)
    return rounded_area, rounded_circumference

r = int(input("Enter radius: "))

area, circumference = circle(r)

print(f"Circle: Area = {area} and Circumference = {circumference}")
