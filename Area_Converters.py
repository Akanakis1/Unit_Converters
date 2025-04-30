print("**************************")
print("**Unit_Converterers_Area**")
print("**************************")

# Display unit options
print("Available Units:")
print(f"1:  Square Meter\n2:  Square Kilometer\n3:  Square Centimeter\n4:  Square Millimeter\n5:  Square Micrometer\n6:  Hectare\n7:  Square Mile\n8:  Square Yard\n9:  Square Foot\n10: Square Inch\n11: Acre\n")

# Conversion TO Square Meter
conversion_factors_to_m_2 = {
    1: 1,               # Square Meter
    2: 0.000001,        # Square Kilometer
    3: 10000,           # Square Centimeter
    4: 1000000,         # Square Millimeter
    5: 1000000000000,   # Square Micrometer
    6: 0.0001,          # Hectare
    7: 3.861018768E-7,  # Square Mile
    8: 1.1959900463,    # Square Yard
    9: 10.763910417,    # Square Foot
    10: 1550.0031,      # Square Inch
    11: 0.0002471054    # Acre
}

unit_names = {
    1: "Square Meter", 2: "Square Kilometer", 3: "Square Centimeter", 4: "Square Millimeter",
    5: "Square Micrometer", 6: "Hectare", 7: "Square Mile", 8: "Square Yard", 9: "Square Foot", 10: "Square Inch",
    11: "Acre"
}

def validate_area(prompt):
    while True:
        try:
            area = float(input(prompt))
            if area <= 0:
                raise ValueError("area must be greater than zero.")
            return area
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
from_unit = validate_unit("Select the unit of area you want to convert FROM (1-11): ")
num_from = validate_area("Enter the area to be converted: ")
to_unit = validate_unit("Select the unit of area you want to convert TO (1-11): ")

def convert_area(value, from_unit, to_unit):
    if from_unit != 1:
        value_in_meters = value / conversion_factors_to_m_2[from_unit]
        converted_value = value_in_meters / conversion_factors_to_m_2[to_unit]
    else:
        # Convert from source unit to meters
        value_in_meters = value * conversion_factors_to_m_2[from_unit]
        # Convert from meters to target unit
        converted_value = value_in_meters / conversion_factors_to_m_2[to_unit]
    return round(converted_value, 4)

# Perform conversion and show result
converted = convert_area(num_from, from_unit, to_unit)
print(f"\n{num_from} {unit_names[from_unit]}(s) ==> {converted} {unit_names[to_unit]}(s)")