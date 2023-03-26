# Stablishing the lists
bank_accounts = []
balances = []

print("\nEnter the names and balances of bank accounts (type: quit when done)")

# The program will ask for the name of the account and the balance until the user types "Quit"
account_name = ""

while account_name.capitalize() != "Quit":
    account_name = input("What is the name of this account? ")
    

    if account_name.capitalize() != "Quit":
        bank_accounts.append(account_name.capitalize())

        account_balance = float(input("What is the balance? "))
        balances.append(account_balance)


# Printing the list with the aacounts and its balances.

print("\nAccount Information:")
for i in range(len(bank_accounts)):
    name = bank_accounts[i]
    balance = balances[i]
    print(f"{i + 1}. {name} - ${balance:,.2f}")


# Printing the total of the sum of the balances.
running_total = 0

for balance in balances:
    running_total += balance
print(f"\nTotal: ${running_total:,.2f}")

# Printing the average of the balances.
average = running_total / len(balances)
print(f"Average: ${average:,.2f}")


# Calculating the highest balance of the accounts.
max_number = -1
max_name = ""

for i in range(len(bank_accounts)):
    name = bank_accounts[i]
    balance = balances[i]

    if balance > max_number:
        max_number = balance
        max_name = name

print(f"Highest balance: {max_name} - ${max_number:,.2f}")


# Updating the account. The program will ask to the user if he wants to update an account until the answer is no.
print()
update = "Yes"

while update == "Yes":
        update = input("Do you want to update an account? ")

        # Asking for the index of the account and the new amount.
        if update.capitalize() == "Yes":
            update_index = int(input("What account index do you want to update? "))
            new_balance = float(input("What's the new amount? "))
            balances[update_index - 1] = new_balance


            # Printing the account information with the new values.
            print("\nAccount Information:")
            for i in range(len(bank_accounts)):
                name = bank_accounts[i]
                balance = balances[i]
                print(f"{i + 1}. {name} - ${balance:,.2f}")

# When the user types "No"
print("Thank You. Goodbye.")