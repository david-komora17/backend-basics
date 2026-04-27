# Random number generator
# First import the random library to access random number functions 

import random 

# Generate a random integer between 1 and 100 
# random.randint(a, b) retunrs a random integer N such that a <= N <= b

random_number = random.randint(1, 100)

# Print the generated random number
print(f"Random number between 1 and 100: {random_number}")

# You can also generate multiple random numbers
print("\n Let's generate 5 more random numbers")

for i in range(5):
    print(f"Number {i+1} : {random.randint(1, 100)}")