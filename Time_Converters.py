print("**************************")
print("**Unit_Converterers_Time**")
print("**************************")

# Display unit options
print("Available Units:")
print(f"1:  Second\n2:  Millisecond\n3:  Microsecond\n4:  Nanosecond\n5:  Picosecond")
print(f"6:  Minute\n7:  Hour\n8:  Day\n9:  Week\n10: Month\n11: Year\n")

# Conversion TO Minute
conversion_factors_to_sec = {
    1:  1,          # Second
    2:  1e-3,       # Millisecond
    3:  1e-6,       # Microsecond
    4:  1e-9,       # Nanosecond
    5:  1e-12,      # Picosecond
    6:  60,         # Minute
    7:  3600,       # Hour
    8:  86400,      # Day
    9:  604800,     # Week
    10: 2.629746e6, # Month (average, 30.44 days)
    11: 3.1556926e7 # Year (average, 365.2425 days)
}

unit_names = {
    1: "Second", 2: "Millisecond", 3: "Microsecond", 4: "Nanosecond",
    5: "Picosecond", 6: "Minute", 7: "Hour", 8: "Day", 9: "Week", 10: "Month",
    11: "Year"
}

def validate_time(prompt):
    while True:
        try:
            time = float(input(prompt))
            if time <= 0:
                raise ValueError("time must be greater than zero.")
            return time
        except ValueError as e:
            print(e)

def validate_unit(prompt):
    while True:
        try:
            unit_val = int(input(prompt))
            if unit_val < 1 or unit_val > 11:
                raise ValueError("Invalid choice. Please enter a number between 1 and 11.")
            return unit_val
        except ValueError as e:
            print(e)

# Input from user
from_unit = validate_unit("Select the unit of time you want to convert FROM (1-11): ")
time_from = validate_time("Enter the time to be converted: ")
to_unit = validate_unit("Select the unit of time you want to convert TO (1-11): ")

def convert_time(value, from_unit, to_unit):
    value_in_sec = value * conversion_factors_to_sec[from_unit]
    converted_value = value_in_sec / conversion_factors_to_sec[to_unit]
    if converted_value < 1e-6:
        return round(converted_value, 12)
    elif converted_value < 1:
        return round(converted_value, 10)
    elif converted_value < 1e6:
        return round(converted_value, 6)
    else:
        return round(converted_value, 0)

# Perform conversion and show result
converted = convert_time(time_from, from_unit, to_unit)
print(f"\n{time_from} {unit_names[from_unit]}(s) ==> {converted} {unit_names[to_unit]}(s)")