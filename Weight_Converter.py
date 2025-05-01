print("****************************")
print("**Unit_Converterers_Weight**")
print("****************************")

# Display unit options
print("Available Units:")
print(f"1:  Kilogram\n2:  Gram\n3:  Milligram\n4:  Metric Ton\n5:  Long Ton")
print("6:  Short Ton\n7:  Pound\n8:  Ounce\n9:  Carrat\n10: Atomic Mass Unit\n")

# Conversion TO Kilogram
conversion_factors_to_kg = {
    1:  1,                # Kilogram
    2:  0.001,            # Gram
    3:  0.000001,         # Milligram
    4:  1000,             # Metric Ton
    5:  1016.0469088,     # Long Ton
    6:  907.18474,        # Short Ton
    7:  0.45359237,       # Pound
    8:  0.028349523125,   # Ounce
    9:  0.0002,           # Carrat
    10: 1.66053906660e-27 # Atomic Mass Unit
}

unit_names = {
    1: "Kilogram", 2: "Gram", 3: "Milligram", 4: "Metric Ton", 5: "Long Ton",
    6: "Short Ton", 7: "Pound", 8: "Ounce", 9: "Carrat", 10: "Atomic Mass Unit"
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
    value_in_kg = value * conversion_factors_to_kg[from_unit]
    converted_value = value_in_kg / conversion_factors_to_kg[to_unit]
    return converted_value

# Perform conversion and show result
converted = convert_weight(num_from, from_unit, to_unit)
print(f"\n{num_from} {unit_names[from_unit]}(s) ==> {converted} {unit_names[to_unit]}(s)")