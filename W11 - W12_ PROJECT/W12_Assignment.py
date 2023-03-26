data_set = []
with open("life-expectancy.csv") as data_file:
    for line in data_file:
        if line.startswith("Entity"): continue; # this will skip the first line, which we don't need
        row = line.split(",")
        new_row = []
        new_row.append(row[0])  #country field
        new_row.append(row[1])  #country code, not used
        new_row.append(int(row[2])) # this is the year field, convert to int
        new_row.append(float(row[3]))  #this is the life expectancy field, convert to float
        data_set.append(new_row)
# find year and country with lowest and  highest life expentancy, since we're looking for a low value, we'll start with a really high value and go lower from here
min_year = None
min_country = None
min_expect = 1000000

max_expect = -1
max_year = None
max_country = None

min_year_selec = None
min_country_selec = None
min_expect_selec = 100000

max_year_selec = None
max_country_selec = None
max_expect_selec = -1

sum = 0

year_select_exp = None
year_select_len = None


user_choice =int(input("Enter the year of interest: "))

for i in data_set:
    new_expect = i[3] # i[3] is the 4th value in the data line, the life expetancy number
    #if we find a new row with a lower expectancy, we capture the data and use it as our lowest expetancy
    year = i[2]
    


    if new_expect < min_expect:
        min_expect = i[3]
        min_year = i[2]
        min_country = i[0]

    if new_expect > max_expect:
        max_expect = i[3]
        max_year = i[2]
        max_country = i[0]


    
    if user_choice == year:
        
        year_select_exp = i[3]
        year_select_len = i[0]

        if new_expect < min_expect_selec:
            min_expect_selec = i[3]
            min_year_selec = i[2]
            min_country_selec = i[0]

        if new_expect > max_expect_selec:
            max_expect_selec = i[3]
            max_year_selec = i[2]
            max_country_selec = i[0]


        sum += year_select_exp
average = sum / len(year_select_len)

 
    
print()    
print(f"{max_country} has the highest life expectancy in {max_year} with {max_expect}")
print(f"{min_country} has the lowest life expectancy in {min_year} with {min_expect}")

print()
print(f"For year {user_choice}:")
print(f"The average is: {average}")
print(f"{max_country_selec} has the highest life expectancy in {max_year_selec} with {max_expect_selec}")
print(f"{min_country_selec} has the lowest life expectancy in {min_year_selec} with {min_expect_selec}")
