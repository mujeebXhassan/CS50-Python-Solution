# Prompt the user for an arithmetic expression
expression = input("Expression: ")

# Split the string by spaces into x, y, z
x, y, z = expression.split(" ")

# Convert x and z from strings to floating-point numbers
x = float(x)
z = float(z)

# Perform the math based on the operator y
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

# Print the result formatted to 1 decimal place
print(f"{result:.1f}")
