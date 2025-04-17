from math import pi
print("Calculate the area of a cone.")
radius = float(input("Enter the raduis: "))
slantheight = float(input("Enter the slant height: "))
answer = radius*pi*slantheight
print(f"The answer is {answer}")