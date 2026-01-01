# Unit & Currency Converters (Python CLI)

A collection of simple, modular **Python command-line (CLI) converters** for common measurement units and currencies.  
Each script is interactive (menu + input validation) and designed to practice clean logic, conversions, and user-friendly prompts.

## Included Converters

- **Area Converter** — `Area_Converters.py`
  Converts between m², km², cm², mm², µm², hectare, square mile, yard, foot, inch, acre.

- **Length Converter** — `Length_Converters.py`
  Converts between meter, kilometer, centimeter, millimeter, micrometer, nanometer, mile, yard, foot, inch, light year.

- **Temperature Converter** — `Temperature_Converters.py`
  Converts between Celsius, Kelvin, and Fahrenheit (includes absolute-zero validation).

- **Time Converter** — `Time_Converters.py`
  Converts between seconds and larger/smaller time units (ms, µs, ns, ps, minutes, hours, days, weeks, months, years).

- **Weight Converter** — `Weight_Converter.py` 
  Converts between kg, g, mg, metric ton, long ton, short ton, lb, oz, carat, and atomic mass unit.

- **Currency Converter** — `Currencies_Converters.py` 
  Converts between multiple currencies (USD, EUR, GBP, JPY, etc.). Uses an external FX library for exchange rates.

## How to Run

### Requirements
- Python 3.8+
- Standard library only for unit converters
- Currency converter requires an external package

### Run a converter
From the repository folder:

```bash
python Area_Converters.py
python Length_Converters.py
python Temperature_Converters.py
python Time_Converters.py
python Weight_Converter.py
python Currencies_Converters.py
