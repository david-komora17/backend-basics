# Simple calculator program
# Get input from the user for the first number
# float() converts the input string to a decimal number 
num1 = float(input("Enter the first number: "))

# Get input for the operator (+, -, *, /)
operator = input("Enter an operator (+, -, *, /): ")

# Get input for the second number
num2 = float(input("Enter the second number: "))

# perform the calculation based on the operator
# using the if/elif/else struture to check which operation to perform 
if operator == "+" :
    result = num1 + num2
    print("f{num1} + {num2} = {result}")

# perform the operation based on the calculator
elif operator == "-" :
    result = num1 - num2
    print("f{num1} - {num2} = {result}")

# perform the operation based on the calculator
elif operator == "*" :
    result = num1 * num2
    print("f{num1} * {num2} = {result}")

# perform the operation based on the calculator
elif operator == "/" :
    if num2 != 0:
        result = num1 / num2
        print("f{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")

else: 
    print("Error: Invalid operator! Please use +, -, *, or /")