print("*********************************")
print("** Unit_Converters_Temperature **")
print("*********************************")

# Display unit options
print("Available Units:")
print(f"1: Celsius\n2: Kelvin\n3: Fahrenheit\n")

unit_names = {1: "Celsius", 2: "Kelvin", 3: "Fahrenheit"}

def validate_unit(prompt):
    while True:
        try:
            unit_val = int(input(prompt))
            if unit_val < 1 or unit_val > 3:
                raise ValueError("Invalid choice. Please enter a number between 1 and 3.")
            return unit_val
        except ValueError as e:
            print(e)

def validate_temperature(prompt):
    while True:
        try:
            temp_val = float(input(prompt))
            if from_unit == 1 and temp_val <=-273.15:
                raise ValueError(f"Celsius can't be below -273.15°.")
            elif from_unit == 2 and temp_val <=0:
                raise ValueError(f"Kelvin can't be below 0°.")
            elif from_unit == 3 and temp_val <=-459.67:
                raise ValueError(f"Fahrenheit can't be below -459.67°")
            return temp_val
        except ValueError as e:
            print(e)

from_unit = validate_unit("Select the unit of temperature you want to convert FROM (1-3): ")
temperature_from = validate_temperature("Enter the temperature to be converted: ")
to_unit = validate_unit("Select the unit of temperature you want to convert TO (1-3): ")

def convert_temperature(value, from_unit, to_unit):
    # Convert input to Celsius as base
    if from_unit == 1:
        temp_c = value
    elif from_unit == 2:
        temp_c = value - 273.15
    elif from_unit == 3:
        temp_c = (value - 32) * 5/9

    # Convert from Celsius to target unit
    if to_unit == 1:
        return round(temp_c, 2)
    elif to_unit == 2:
        return round(temp_c + 273.15, 2)
    elif to_unit == 3:
        return round((temp_c * 9/5) + 32, 2)

converted_value = convert_temperature(temperature_from, from_unit, to_unit)

print(f"\n{temperature_from:.2f}° {unit_names[from_unit]} = {converted_value:.2f}° {unit_names[to_unit]}")