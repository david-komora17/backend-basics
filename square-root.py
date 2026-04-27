# import the math library to access the square root 
import math

# Get input from the user for the number
# float() allows decimal numbers
number = float(input("Enter a number to find its square root: "))

# check if the number is non-negative(square roots of negative numbers are imaginary)
if number >= 0:
    
# calculate square root using math.sqrt() function 
# math.sqrt() returns the square root of the number

    square_root = math.sqrt(number)

    # Print the result
    #:.2f formats the number to 2 d.p
    print(f"the square root of {number} is {square_root:.2f}")

    #show more decimal places
    print(f"More precise: the square root of {number} is {square_root}")
else: 
    # handle negative numbers
    print("Error: Cannot calculate square root of a negative number!")
    print("Square root of a negative number is an imaginary number.")

    # Bonus: Demonstrate using square root numbers with other numbers
    print("\n--- Some examples ---")
    print(f"square root of 16: {math.sqrt(16)}")
    print(f"square root of 2.25: {math.sqrt(2.25)}")