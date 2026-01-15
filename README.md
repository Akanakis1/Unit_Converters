# Unit & Currency Converters — Python CLI Utilities

This repository contains a collection of small, modular Python command-line utilities
for converting common measurement units and currencies.

The focus of this project is on **clean control flow, input validation, and modular design**,
rather than advanced analytics or machine learning.

---

## Project Purpose

This project exists to demonstrate:
- basic Python proficiency,
- structured program flow in CLI applications,
- robust input validation and user prompts,
- separation of concerns across small, focused scripts.

It complements analytics-focused projects by showing solid programming fundamentals.

---

## Included Converters

### Area Converter — `Area_Converters.py`
Converts between:
- square meters, kilometers, centimeters, millimeters, micrometers
- hectares, acres
- square miles, yards, feet, inches

---

### Length Converter — `Length_Converters.py`
Converts between:
- metric units (m, km, cm, mm, µm, nm)
- imperial units (mile, yard, foot, inch)
- astronomical unit (light year)

---

### Temperature Converter — `Temperature_Converters.py`
Converts between:
- Celsius
- Fahrenheit
- Kelvin

Includes validation for physically invalid inputs (e.g. below absolute zero).

---

### Time Converter — `Time_Converters.py`
Converts between:
- seconds, milliseconds, microseconds, nanoseconds
- minutes, hours, days, weeks, months, years

---

### Weight Converter — `Weight_Converter.py`
Converts between:
- kilograms, grams, milligrams
- metric tons, long tons, short tons
- pounds, ounces, carats, atomic mass units

---

### Currency Converter — `Currencies_Converters.py`
Converts between multiple currencies (USD, EUR, GBP, JPY, etc.)
using an external foreign-exchange rate library.

This script demonstrates:
- external package usage,
- dynamic rate retrieval,
- separation between logic and data sources.

---

## Repository Structure

├── Area_Converters.py  
├── Length_Converters.py  
├── Temperature_Converters.py  
├── Time_Converters.py  
├── Weight_Converter.py  
├── Currencies_Converters.py  
└── README.md  

---

## How to Run

### Requirements
- Python 3.8+
- Unit converters use the Python standard library only
- Currency converter requires an external FX package (see script imports)

### Running a Converter

From the repository directory:

```bash
python Area_Converters.py
python Length_Converters.py
python Temperature_Converters.py
python Time_Converters.py
python Weight_Converter.py
python Currencies_Converters.py
