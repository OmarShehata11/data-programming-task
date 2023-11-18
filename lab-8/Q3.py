def fahrenheit_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  kelvin = celsius + 273.15
  return celsius, kelvin



fahrenheit = int(input("enter fahrenheit > "))

celsius, kelvin = fahrenheit_to_celsius(fahrenheit)

print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius and {kelvin} Kelvin")
