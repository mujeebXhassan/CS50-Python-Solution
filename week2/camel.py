# Prompt the user for a camelCase variable name
camel = input("camelCase: ")

# Create an empty string to build the snake_case version
snake = ""

# Loop through every single character in the user's input
for char in camel:
    # Check if the current character is an uppercase letter
    if char.isupper():
        # Add an underscore and the lowercase version of the letter
        snake += "_" + char.lower()
    else:
        # If it's already lowercase, just add the exact character
        snake += char

# Print the final converted string
print(f"snake_case: {snake}")
