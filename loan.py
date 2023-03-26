print("\nPlease answer to the following questions with a 1-10 rating.")

# Questions
loan_size = int(input("\nHow large is the loan? "))
credit_history = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))

is_loan = False

# Loan size at least 5.
if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        is_loan = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            is_loan = True
        else:
            is_loan = False

    else:
        is_loan = False

# Loan size lower than 5.
else:
    if credit_history < 4:
        is_loan = False
    elif income >= 7 or down_payment >= 7:
        is_loan = True
    elif income >= 4 and down_payment >= 4:
        is_loan = True
    else:
        is_loan = False


if is_loan:
     print("\nApproved.")

if not is_loan:
    print("\nRejected.")