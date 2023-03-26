print()
# A positive number.
number = int(input("Please type a positive number: "))

while number < 0:
    print("Sorry, that's a negative number. Please try again.")
    number = int(input("Please type a positive number: ")) 


print(f"The number is {number}.")

print()



# Candy example
candy = input("May I have a piece of candy? ")

# I used "different to" in order to avoid an error with words like "maybe", "tomorrow" or something different than yes or no.
while candy.lower() != "yes":
   candy = input("May I have a piece of candy? ")


print("Thank You.") 
