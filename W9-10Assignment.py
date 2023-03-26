print()
print("Welcome to the Shopping Cart Program!")

shopping_list = []
price_list = []

# MENU

menu = 0

while menu != 5: 
    print("\nPlease select one of the following:")
    print("1. Add item\n2. View chart\n3. Remove item\n4. Compute total\n5. Quit")

    print()
    menu = int(input("Please enter an action (type the number): "))
    

    if menu == 1:
        name_item = input("\nWhat item would you like to add? ")
        price_item = float(input(f"What's the price of '{name_item}'? "))
        shopping_list.append(name_item.capitalize())
        price_list.append(price_item)

        print(f"'{name_item.capitalize()}' has been added to the cart.")

    if menu == 2:
        print("The contents of the shopping cart are: ")
    
        for i in range(len(shopping_list)):
            item = shopping_list[i]
            price = price_list[i]
            print(f"{i + 1}. {item} - ${price:,.2f}")

    if menu == 3:
        index_item = int(input("Which item would you like to remove? "))
        price_list.pop(index_item - 1)
        shopping_list.pop(index_item - 1)

        print("Item removed.")

    if menu == 4:
        running_total = 0
        
        for amount in price_list:
            running_total += amount
        
        print(f"The total price of the items in the shopping cart is ${running_total:,.2f}")

print("Thank you. Goodbye.")