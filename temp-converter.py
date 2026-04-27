# Exercise 4: Convert Celsius to Fahrenheit

# Formula: Fahrenheit = (Celsius × 9/5) + 32

# Prompt user for Celsius temperature
celsius = input("Enter temperature in Celsius: ")

# Convert input to float (allows decimal temperatures)
celsius = float(celsius)

# Calculate Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Print the converted temperature
print(f"{celsius}°C is equal to {fahrenheit}°F")

# Bonus: Round to 1 decimal place for cleaner output
fahrenheit_rounded = round(fahrenheit, 1)
print(f"Rounded: {celsius}°C = {fahrenheit_rounded}°F")

# Bonus: Conversion both ways
print("\n--- Quick Reference ---")
print("Freezing point: 0°C = 32°F")
print("Boiling point: 100°C = 212°F")
print("Room temperature: 22°C = 71.6°F")