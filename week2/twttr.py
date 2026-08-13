# Prompt the user for a string of text
text = input("Input: ")

# Create an empty string to build the final output
output = ""

# Define all the vowels we want to look for (both lower and uppercase)
vowels = "aeiouAEIOU"

# Loop through every single character in the user's input
for char in text:
    # If the character is NOT in our string of vowels, keep it
    if char not in vowels:
        output += char

# Print the final resulting string
print(f"Output: {output}")
