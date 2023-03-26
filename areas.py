# Area of the square
square = float(input("What's the length of a side of the square? "))
operation = square**2
area_square = f"The area of the square is: {operation}"
print(area_square)

# Area of the rectangle
length = float(input("\nWhat's the length of the rectangle? "))
width = float(input("\nWhat's the width of the rectangle? "))
area = length*width
print(f"The area of the rectangle is: {area}")

# Area of the circle
pi = 3.14
radius = float(input("\nWhat's the radius of the circle? "))
circle = pi*(radius**2)
print(f"The area of the circle is: {circle}")