# main.py

from converter import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_celsius,
    kelvin_to_fahrenheit
)

def convert_temperature(value, unit):
    unit = unit.lower()
    
    if unit in ["celsius", "c"]:
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        print(f"\n{value}° Celsius is:")
        print(f"➡ {f:.2f}° Fahrenheit")
        print(f"➡ {k:.2f} K (Kelvin)")

    elif unit in ["fahrenheit", "f"]:
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        print(f"\n{value}° Fahrenheit is:")
        print(f"➡ {c:.2f}° Celsius")
        print(f"➡ {k:.2f} K (Kelvin)")

    elif unit in ["kelvin", "k"]:
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        print(f"\n{value} K (Kelvin) is:")
        print(f"➡ {c:.2f}° Celsius")
        print(f"➡ {f:.2f}° Fahrenheit")

    else:
        print(" Invalid unit. Use Celsius, Fahrenheit, or Kelvin.")

if __name__ == "__main__":
    print(" Welcome to the Temperature Conversion Program ")
    try:
        temp = float(input("Enter the temperature value: "))
        unit = input("Enter the unit (Celsius, Fahrenheit, Kelvin): ")
        convert_temperature(temp, unit)
    except ValueError:
        print(" Please enter a valid number.")
