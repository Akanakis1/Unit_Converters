print("****************************")
print("**Unit_Converterers_Length**")
print("****************************")

# Display unit options
print("Available Units:")
print(f"1:  Meter\n2:  Kilometer\n3:  Centimeter\n4:  Millimeter\n5:  Micrometer\n6:  Nanometer\n7:  Mile\n8:  Yard\n9:  Foot\n10: Inch\n")

# Conversion TO meters
conversion_factors_to_meter = {
    1: 1,         # Meter
    2: 1000,      # Kilometer
    3: 0.01,      # Centimeter
    4: 0.001,     # Millimeter
    5: 1e-6,      # Micrometer
    6: 1e-9,      # Nanometer
    7: 1609.3444, # Mile
    8: 0.91444,   # Yard
    9: 0.3048,    # Foot
    10: 0.0254    # Inch
}

unit_names = {
    1: "Meter", 2: "Kilometer", 3: "Centimeter", 4: "Millimeter",
    5: "Micrometer", 6: "Nanometer", 7: "Mile", 8: "Yard", 9: "Foot", 10: "Inch"
}

def validate_length(prompt):
    while True:
        try:
            length = float(input(prompt))
            if length <= 0:
                raise ValueError("Length must be greater than zero.")
            return length
        except ValueError as e:
            print(e)

def validate_unit(prompt):
    while True:
        try:
            unit_val = int(input(prompt))
            if unit_val < 1 or unit_val > 10:
                raise ValueError("Invalid choice. Please enter a number between 1 and 10.")
            return unit_val
        except ValueError as e:
            print(e)

# Input from user
from_unit = validate_unit("Select the unit of length you want to convert FROM (1-10): ")
num_from = validate_length("Enter the length to be converted: ")
to_unit = validate_unit("Select the unit of length you want to convert TO (1-10): ")

def convert_length(value, from_unit, to_unit):
    if from_unit != 1:
        value_in_meters = value / conversion_factors_to_meter[from_unit]
        converted_value = value_in_meters / conversion_factors_to_meter[to_unit]
    else:
        # Convert from source unit to meters
        value_in_meters = value * conversion_factors_to_meter[from_unit]
        # Convert from meters to target unit
        converted_value = value_in_meters / conversion_factors_to_meter[to_unit]
    return round(converted_value, 4)

# Perform conversion and show result
converted = convert_length(num_from, from_unit, to_unit)
print(f"\n{num_from} {unit_names[from_unit]}(s) ==> {converted} {unit_names[to_unit]}(s)")