def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def celsius_to_kelvin(celsius):
    return celsius + 273.15
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Main program
print("Temperature Converter")
print("Choose conversion type:")
print("1. Celsius to Fahrenheit and Kelvin")
print("2. Fahrenheit to Celsius and Kelvin")
print("3. Kelvin to Celsius and Fahrenheit")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    print(f"Fahrenheit: {celsius_to_fahrenheit(c):.2f}")
    print(f"Kelvin: {celsius_to_kelvin(c):.2f}")
elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    print(f"Celsius: {fahrenheit_to_celsius(f):.2f}")
    print(f"Kelvin: {fahrenheit_to_kelvin(f):.2f}")
elif choice == 3:
    k = float(input("Enter temperature in Kelvin: "))
    print(f"Celsius: {kelvin_to_celsius(k):.2f}")
    print(f"Fahrenheit: {kelvin_to_fahrenheit(k):.2f}")
else:
    print("Invalid choice. Please select 1, 2, or 3.")
