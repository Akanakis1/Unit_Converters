print("****************************")
print("**Unit_Converterers_Weight**")
print("****************************")

# Display unit options
print("Available Units:")
print(f"1:  Kilogram\n2:  Gram\n3:  Milligram\n4:  Metric Ton\n5:  Long Ton\n6:  Short Ton\n7:  Pound\n8:  Ounce\n9:  Carrat\n10: Atomic Mass Unit\n")

# Conversion TO Kilogram
conversion_factors_to_kg = {
    1:  1,                # Kilogram
    2:  1000,             # Gram
    3:  1000000,          # Milligram
    4:  0.001,            # Metric Ton
    5:  0.0009842073,     # Long Ton
    6:  0.0011023122,     # Short Ton
    7:  2.2046244202,     # Pound
    8:  35.273990723,     # Ounce
    9:  5000,             # Carrat
    10: 6.022136652E+26   # Atomic Mass Unit
}

unit_names = {
    1: "Kilogram", 2: "Gram", 3: "Metric Ton", 4: "Metric Ton",
    5: "Long Ton", 6: "Short Ton", 7: "Pound", 8: "Ounce", 9: "Carrat", 10: "Atomic Mass Unit"
}

def validate_weight(prompt):
    while True:
        try:
            weight = float(input(prompt))
            if weight <= 0:
                raise ValueError("Weight must be greater than zero.")
            return weight
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
from_unit = validate_unit("Select the unit of Weight you want to convert FROM (1-10): ")
num_from = validate_weight("Enter the Weight to be converted: ")
to_unit = validate_unit("Select the unit of Weight you want to convert TO (1-10): ")

def convert_weight(value, from_unit, to_unit):
    if from_unit != 1:
        value_in_kg = value / conversion_factors_to_kg[from_unit]
        converted_value = value_in_kg * conversion_factors_to_kg[to_unit]
    else:
        value_in_kg = value * conversion_factors_to_kg[from_unit]
        converted_value = value_in_kg * conversion_factors_to_kg[to_unit]
    return round(converted_value, 4)

# Perform conversion and show result
converted = convert_weight(num_from, from_unit, to_unit)
print(f"\n{num_from} {unit_names[from_unit]}(s) ==> {converted} {unit_names[to_unit]}(s)")