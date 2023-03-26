print('\nPlease enter the items of the shopping list (type "quit" to finish):')

# Declaring the list.
shopping_list = []
menu = ""

# The program will continue asking for an item to add it to the shopping list until the user type "quit".
while menu != "quit": 
    menu = input("Item: ")

    if menu != "quit":
        shopping_list.append(menu.capitalize())

# Printing the list.
print()        
print("The shopping list is: ")
    
for item in shopping_list:
    print(f"{item}")


# Printing the list with indexes starting from 1.
print()
print("The shopping list with indexes is: ")

for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i + 1}. {item}")


# Asking the user if he wants to change an item from the list.
user_choice = input("\nDo you want to change an item? ")


# The answer is "Yes"
if user_choice.capitalize() == "Yes":

    index = -1

    # The program is asking for the number of the item. It will continue asking until the user type 0 to finish.
    while index != 0:
        index = int(input("\nWhich item would you like to change? (Type 0 to finish) "))
    
        # The program is asking for the new item.
        if index != 0: 
            new_item = input("What's the new item? ")

            shopping_list[index - 1] = new_item.capitalize()

    # Printing the new list with indexes.
    print()
    print("The shopping list with indexes is: ")

    for i in range(len(shopping_list)):
        item = shopping_list[i]
        print(f"{i + 1}. {item}")

    print("\nThank you. Goodbye")

# nswer is "No"
if user_choice.capitalize() == "No":
    print("Thank you. Goodbye")
