# Game Title: Treasure Hunt

# Variables
treasures = ["gold", "silver", "diamond"]
inventory = []

# Introduction
print("Welcome to Treasure Hunt!")
print("You are a treasure hunter, looking for valuable treasures.")
print("You have heard of three treasures: gold, silver, and diamond.")
print("You have to find all three to win the game.")

# Main Game Loop
while len(inventory) < len(treasures):
    print("You are in a room. You see a door and a chest.")
    choice = input("Do you want to (1) open the door or (2) open the chest? ")
    if choice == "1":
        print("You go through the door and find yourself in another room.")
    elif choice == "2":
        item = treasures[len(inventory)]
        print("You find a " + item + " in the chest.")
        inventory.append(item)

# End of the game
print("Congratulations! You have found all the treasures: " + str(inventory))
print("You won the Treasure Hunt game!")
