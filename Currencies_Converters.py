from forex_python.converter import CurrencyRates #pip install forex-python
print("********************************")
print("**Unit_Converterers_Currencies**")
print("********************************")

# Display unit options
print("Available Currencies:")
print(f"1: USD ($)\n2: EUR (€)\n3: GBP (£)\n4: JPY (¥)\n5: AUD ($)")
print(f"6: CAD ($)\n7: CHF\n8: CNY (¥)\n9: INR (₹)\n10: RUB (₽)")
print(f"11: BRL (R$)\n12: ZAR (R)\n13: MXN ($)\n14: SGD ($)\n15: NZD ($)")
print(f"16: HKD (HK$)\n")

unit_names = {
    1: "USD", 2: "EUR", 3: "GBP", 4: "JPY", 5: "AUD",
    6: "CAD", 7: "CHF", 8: "CNY", 9: "INR", 10: "RUB",
    11: "BRL", 12: "ZAR", 13: "MXN", 14: "SGD", 15: "NZD",
    16: "HKD"
}

def validate_unit(prompt):
    while True:
        try:
            unit_val = int(input(prompt))
            if unit_val < 1 or unit_val > 16:
                raise ValueError("Invalid choice. Please enter a number between (1-16).")
            return unit_val
        except ValueError as e:
            print(e)

def validate_amount(prompt):
    while True:
        try:
            weight = float(input(prompt))
            if weight <= 0:
                raise ValueError("Amount must be greater than zero.")
            return weight
        except ValueError as e:
            print(e)

# Get user input
from_unit_idx = validate_unit("Select the currency to convert FROM (1-16): ")
to_unit_idx = validate_unit("Select the currency to convert TO (1-16): ")
amount = validate_amount("Enter the amount to be converted: ")

from_currency = unit_names[from_unit_idx]
to_currency = unit_names[to_unit_idx]

c = CurrencyRates()

# Perform the conversion
try:
    converted = c.convert(from_currency, to_currency, amount)
    print(f"\n{amount:.2f} {from_currency} <==> {converted:.2f} {to_currency}")
except Exception as e:
    print(f"\nError during conversion: {e}")
