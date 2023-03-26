
print("\nThink in two numbers.\n")
first_int = int(input("What's the first number? "))
second_int = int(input("What's the second number?"))

print()

if first_int > second_int:
    print("The first number is greater.")
else:
    print("The first number is not greater.")

if first_int == second_int:
    print("The number are equal.")
else: 
    print("The numbers are not equal.")

if second_int > first_int:
    print("The second number is greater.")
else:
    print("The second number is not greater")

print()

fav_animal = input("What's your favorite animal? ")
my_fav_animal = "Panda"

if fav_animal.capitalize() == my_fav_animal:
    print("That's my favorite animal too!")
else:
    print("That's is not my favorite")

print()