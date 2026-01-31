# import math

# def circle_stats(radius):
#     area = math.pi * radius ** 2
#     circumference = 2 * math.pi * radius
#     return area, circumference

# area, circumference = circle_stats(float(input("Radius: ")))
# print("Area : is ", area)
# print("Circumferene : ", circumference)

# MORE IMPROVED VERSION

import math


def circle_stats(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return area, circumference


print("===================================")
print("        🔵 CIRCLE CALCULATOR 🔵")
print("===================================")

radius = float(input("👉 Enter the radius of the circle: "))

area, circumference = circle_stats(radius)

print("\n📐 Circle Details")
print("-----------------------------------")
print(f"✅ Radius        : {radius}")
print(f"✅ Area          : {area:.2f}")
print(f"✅ Circumference : {circumference:.2f}")

print("\n✨ Calculation Completed Successfully ✨")
