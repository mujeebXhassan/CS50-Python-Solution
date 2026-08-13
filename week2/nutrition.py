# Create a dictionary of the FDA's top 20 raw fruits and their calories
# All keys are lowercase to make searching easier
fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

# Prompt the user for an item and immediately convert it to lowercase
item = input("Item: ").lower()

# Check if the user's item exists as a key in our dictionary
if item in fruits:
    # If it does, print the corresponding calorie value
    print(f"Calories: {fruits[item]}")
