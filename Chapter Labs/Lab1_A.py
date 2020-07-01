# Create a program that asks the user for a temperature in Fahrenheit
# Prints the temperature in Celsius.

print("Farhenheit to Celcius Calculator")
print("--------------------------------")
temp_farhenheit = float(input("Enter your temperature in Farenheit: "))
temp_celsius = ((temp_farhenheit-32)*5)/9
print("Temperature in Celsius is: ", temp_celsius)
