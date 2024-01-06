# Vending machine program in python 

# Start up with some introduction 
print("hello......")
print("Welcome to my vending machine program!! How can i help you.")

# Program

print("here are available options in the list.")

# Start up with the list of each items. 

categories = {
    "coffee": 50.00,
    "hot chocolate": 30.00,
    "hot tea": 10.00,
    "iced coffee": 30.00,
    "milk tea": 30.00,
    "juice": 10.00,
    "chocolate milk": 20.00,
    "soda": 15.00,
    "chips": 25.00,
    "chocolate bar": 10.00,
    "ice cream": 15.00,
    "candies": 10.00
}

print(categories)
change = 10.00
while True:
    # ... (the same code as before)

    choice = input("\nEnter the name of the item you want to purchase or 'quit' to exit: ")
    if choice.lower() == "quit":
        break

    # Check if the selected item is available in the vending machine
    if choice in categories:
        # Calculate the total amount required by the user
        total_amount = categories[choice]

        # Check if the user has enough balance
        if total_amount <= change:
            # Add a confirmation prompt
            confirmation = input(f"\nYou have selected {choice} for ${total_amount}. Confirmed? (yes/no): ")
            if confirmation.lower() == "yes":
                print(f"\nHere is your {choice}.")
                change -= total_amount
                print(f"Your remaining balance is ${change}.")
            else:
                print("\nPurchase cancelled. Please choose a different item.")
        else:
            print("\nYou do not have enough balance for this item. Please add more money.")
    else:
        print("\nInvalid item selected. Please select a valid item.")

        

