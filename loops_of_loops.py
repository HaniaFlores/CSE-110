import math
user_input = int(input("How many columns and rows do you want in your multiplication table? "))
range_size = user_input + 1
max_number = user_input * user_input
# digits = 2
# if max_number > 100:
#     digits = 3
digits = int(math.log10(max_number)) + 1

for row_number in range(1, range_size):

    for column_number in range(1, range_size):
        number = row_number * column_number
        print(f"{number:{digits}}" , end=" ")
    print( )
