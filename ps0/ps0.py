
import math

# Step 1: Ask the user to enter a number "x"
x = int(input("Enter a number x: "))

# Step 2: Ask the user to enter a number "y"
y = int(input("Enter a number y: "))

# Step 3: Print out number "x", raised to the power "y"
result = x ** y
print(f"{x} raised to the power {y} is: {result}")

# Step 4: Print out the log (base 2) of "x"
log_result = math.log2(x)
print(f"The log (base 2) of {x} is: {log_result}")