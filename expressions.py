# Exercise 3: Evaluate expressions with given variables
width = 17
height = 12.0

# Expression 1: Integer division
print("width // 2 =", width // 2)        # Result: 8 (int)
print("Type:", type(width // 2))         # <class 'int'>

# Expression 2: Float division
print("width / 2.0 =", width / 2.0)      # Result: 8.5 (float)
print("Type:", type(width / 2.0))        # <class 'float'>

# Expression 3: Division with float
print("height / 3 =", height / 3)        # Result: 4.0 (float)
print("Type:", type(height / 3))         # <class 'float'>

# Expression 4: Order of operations
print("1 + 2 * 5 =", 1 + 2 * 5)          # Result: 11 (int)
print("Type:", type(1 + 2 * 5))          # <class 'int'>

# Summary table
print("\n--- Summary ---")
print(f"{'Expression':<15} {'Value':<10} {'Type':<10}")
print(f"{'width//2':<15} {width//2:<10} {type(width//2):<10}")
print(f"{'width/2.0':<15} {width/2.0:<10} {type(width/2.0):<10}")
print(f"{'height/3':<15} {height/3:<10} {type(height/3):<10}")
print(f"{'1+2*5':<15} {1+2*5:<10} {type(1+2*5):<10}")