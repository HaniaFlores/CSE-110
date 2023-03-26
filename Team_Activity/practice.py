people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

min_age = 999
min_name = ""

for line in people:
    line = line.strip()
    parts = line.split()

    name = parts[0]
    age = int(parts[1])

    if age < min_age:
        min_name = name 
        min_age = age
        

    print(f"{name} - {age}")

print()    
print(f"Youngest:{min_name} - {min_age}")