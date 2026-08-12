# Prompt the user for the answer
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Clean the user's input: remove whitespace and make it lowercase
answer = answer.strip().lower()

# Check if the answer is one of the accepted variations
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")
