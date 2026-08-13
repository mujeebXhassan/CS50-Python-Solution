# The cost of a Coke is always 50 cents
amount_due = 50

# Keep running the loop as long as the user still owes money
while amount_due > 0:
    # Tell the user how much is still owed
    print(f"Amount Due: {amount_due}")

    # Prompt the user to insert a coin (convert their input to an integer)
    coin = int(input("Insert Coin: "))

    # Only accept valid coins: 25, 10, or 5
    if coin in [25, 10, 5]:
        # Subtract the accepted coin from the total amount due
        amount_due -= coin

# Once the loop finishes (amount_due is 0 or less), calculate the change
# If amount_due is negative (e.g., -5), abs() turns it into a positive number (5)
change_owed = abs(amount_due)

# Print the final change owed
print(f"Change Owed: {change_owed}")
