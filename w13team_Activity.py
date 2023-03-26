import math

# Area of a square.
print()
side = float(input("What is the length of a side of the square? "))
area = side ** 2
print(f"The area of the square is: {area:.1f}")

# Area of a rectangle.
print()
length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the rectangle? "))
area = length * width
print(f"The area of the rectangle is: {area:.1f}")

# Area of a circle.
print()
radius = float(input("What is the radius of the circle? "))
area = math.pi * (radius ** 2)
print(f"The area of the circle is: {area:.1f}")

# Stretch 2: Many areas from one value.
value = float(input("\nWhat is the value to be used? "))

# Areas
area_square = value ** 2
area_circle = math.pi * (value ** 2)
volume_cube = value ** 3
volume_sphere = (4/3) * math.pi * (value ** 3)

print(f"Area of a square: {area_square:.1f}")
print(f"Area of a circle: {area_circle:.1f}")
print(f"Volume of a cube: {volume_cube:.1f}")
print(f"Volume of a sphere: {volume_sphere:.1f}")

# Stretch 3: Display the areas in cm^2.

# Area of a square.
print()
side = float(input("What is the length of a side of the square (in cm)? "))
area = side ** 2
print(f"The area of the square is: {area:.1f} cm\N{superscript two}")
print(f"The area of the square is: {area / 10000:.4f} m\N{superscript two}")

# Area of a rectangle.
print()
length = float(input("What is the length of the rectangle (in cm)? "))
width = float(input("What is the width of the rectangle? (in cm)"))
area = length * width
print(f"The area of the rectangle is: {area:.1f} cm\N{superscript two}")
print(f"The area of the rectangle is: {area / 10000:.4f} m\N{superscript two}")

# Area of a circle.
print()
radius = float(input("What is the radius of the circle (in cm)? "))
area = math.pi * (radius ** 2)
print(f"The area of the circle is: {area:.1f} cm\N{superscript two}")
print(f"The area of the circle is: {area / 10000:.4f} m\N{superscript two}")