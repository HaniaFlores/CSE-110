"""
Hania Flores
Purpose: Compute windchill with the given temperature.
"""
print()
temperature = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ")

def con_c_to_f(temperature):
    new_temp = temperature * (9/5) + 32
    return new_temp


def compute_wind_chill(temperature,wind_speed):
    wind_chill = 35.74 + (0.6215 * temperature) - 35.75 * (wind_speed ** 0.16) + (0.4275 * temperature) * (wind_speed ** 0.16)
    return wind_chill

if unit.upper() == "F":
    for i in range (5, 61, 5):
        wind_speed = i
        compute_wind_chill(temperature,wind_speed)
        print(f"At temperature {temperature:.1f}{unit.upper()}, and wind speed {wind_speed} mph, the windchill is:{compute_wind_chill(temperature,wind_speed):.2f}{unit.upper()}") 

# Convert C to F
if unit.upper() == "C":
    for i in range (5, 61, 5):
        wind_speed = i
        new_temp = con_c_to_f(temperature)
        compute_wind_chill(new_temp,wind_speed)
        print(print(f"At temperature {new_temp:.1f}F, and wind speed {wind_speed} mph, the windchill is:{compute_wind_chill(new_temp,wind_speed):.2f}F"))
