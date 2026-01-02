"""
MY FIRST PYTHON PROGRAM: CIRCLE AREA
=====================================
This is a very simple program for Python beginners.
It does one thing: calculates circle area.
"""

# 1. We need the pi (π) number
# In Python, it's in the "math" library
import math

# 2. Ask the user for the radius
print("Hello! I will calculate the area of a circle.")
print("I need you to tell me the radius.")

# Ask for radius and convert to number
radius_text = input("What is the circle's radius? ")
radius = float(radius_text)  # Convert text to number

# 3. Calculate the area
# Formula: area = π × radius × radius
area = math.pi * radius * radius

# 4. Show the result
print("\n" + "★" * 30)
print(f"RESULT:")
print(f"Circle radius: {radius}")
print(f"Area calculated: {area}")
print(f"Rounded area: {round(area, 2)}")
print("★" * 30)

# 5. Extra information (optional)
print("\n" + "-" * 30)
print("DID YOU KNOW...?")
print(f"The value of π (pi) is: {math.pi}")
print(f"π has many decimals: {math.pi:.10f}")
print("-" * 30)

print("\nThank you for using my program! 😊")
