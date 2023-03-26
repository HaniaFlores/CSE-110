# Asking for the meal price
child_price = float(input("\nWhat's the price of a child's meal? "))
adult_price = float(input("What's the price of an adult's meal? "))

# Asking for the number of children and adults
child_number = int(input("\nHow many children are there? "))
adult_number = int(input("How many adults are there? "))

# Total Meals
child_subtotal = child_number*child_price
adult_sub = adult_price*adult_number

meal = child_subtotal + adult_sub

# Drinks
print("\nDrinks Menu\
\nCoke: $3.99\
\nOrange Juice: $3.49")

coke = int(input("\nHow many cokes? "))
juice = int(input("How many juices? "))

coke_total = coke * 3.99
juice_total = juice * 3.49
drinks = coke_total + juice_total

# Desserts
print("\nDesserts Menu\
\nSlice of Cake: $5.50\
\nIce Cream: $4.50")

cake = int(input("\nHow many slices of cake? "))
ice_cream = int(input("How many ice creams? "))
cake_total = cake * 5.50
ice_cream_total = ice_cream * 4.50
desserts = cake_total + ice_cream_total

# Asking the Sales Tax Rate
tax_rate = float(input("\nWhat's the sales tax rate? "))

# Subtotal
subtotal = meal + drinks + desserts
print(f"\nSubtotal: ${subtotal:.2f}")

# Sales Tax
taxes = subtotal * (tax_rate/100)
print(f"Sales Tax: ${taxes:.2f}")

# Total
total = subtotal + taxes
print(f"Total: ${total:.2f}")

# Payment
amount = float(input("\nWhat's the payment amount? "))
change = amount - total
print(f"Change: ${change:.2f}\
\n\nHave a nice day!\n")
