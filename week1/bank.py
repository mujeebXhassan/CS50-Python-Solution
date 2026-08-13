# Prompt the user for a greeting
greeting = input("Greeting: ")

# Clean the input: remove leading/trailing spaces and convert to lowercase
greeting = greeting.strip().lower()

# Check the conditions and print the correct penalty amount
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
