print("**************************")
print("**Unit_Converterers_Time**")
print("**************************")

# Display unit options
print("Available Units:")
print(f"1:  Second\n2:  Millisecond\n3:  Microsecond\n4:  Nanosecond\n5:  Picosecond\n6:  Minute\n7:  Hour\n8:  Day\n9:  Week\n10: Month\n11: Year\n")

# Conversion TO Minute
conversion_factors_to_sec = {
    1:  60,             # Second
    2:  60000,          # Millisecond
    3:  60000000,       # Microsecond
    4:  60000000000,    # Nanosecond
    5:  60000000000000, # Picosecond
    6:  1,              # Minute
    7:  0.016666666667, # Hour
    8:  0.000694444444, # Day
    9:  0.0000992063,   # Week
    10: 0.0000228154,   # Month
    11: 0.0000019013    # Year
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

def convert_time(time, from_unit, to_unit):
    if from_unit != 6:
        time_in_sec = time / conversion_factors_to_sec[from_unit]
        converted_time = time_in_sec * conversion_factors_to_sec[to_unit]
    else:
        time_in_sec = time * conversion_factors_to_sec[from_unit]
        converted_time = time_in_sec * conversion_factors_to_sec[to_unit]
    return round(converted_time, 2)

# Perform conversion and show result
converted = convert_time(time_from, from_unit, to_unit)
print(f"\n{time_from} {unit_names[from_unit]}(s) ==> {converted} {unit_names[to_unit]}(s)")