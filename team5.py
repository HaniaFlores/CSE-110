grade = float(input("Enter the points earned: "))

sign = " "
letter = " "
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B" 
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

if grade % 10 >= 7:
    sign = "+"
elif grade % 10 < 3:
    sign = "-"
else:
    sign = ""

if grade >= 93:
    sign = ""
if letter == "F":
    sign = ""

print(f"Your grade is {letter}{sign}.")

if grade >= 70:
    print("Congratulations you passed the course.")
else:
    print("Never give up, just keep doing your BEST.")
