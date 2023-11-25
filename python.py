import random

# Character class
class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        self.inventory = []

    def is_alive(self):
        return self.health > 0

    # More character methods...

# Function to create character
def create_character():
    name = input("Enter your character's name: ")
    return Character(name, 100, 10)

# Function to create enemy
def create_enemy():
    enemies = [
        Character("Goblin", 50, 5),
        Character("Ogre", 100, 10),
        Character("Dragon", 200, 20)
    ]
    return random.choice(enemies)

# Function to attack
def attack(attacker, defender):
    damage = random.randint(0, attacker.attack)
    defender.health -= damage
    print("{} attacks {} and deals {} damage!".format(attacker.name, defender.name, damage))

# Function to print health
def print_health(character):
    print("{} has {} health.".format(character.name, character.health))

# Function to print inventory
def print_inventory(character):
    print("{} has {} items.".format(character.name, len(character.inventory)))
    for item in character.inventory:
        print(item)

# Function to add item to inventory
def add_item(character, item):
    character.inventory.append(item)

# Function to remove item from inventory
def remove_item(character, item):
    character.inventory.remove(item)

# Function to print options
def print_options():
    print("1. Attack")
    print("2. Heal")
    print("3. Run")

# Function to get user input
def get_input():
    valid_input = False
    while not valid_input:
        choice = input("Choose an option: ")
        if choice in ["1", "2", "3"]:
            valid_input = True
        else:
            print("Invalid input.")
    return choice

# Function to get user input for healing
def get_healing_input():
    valid_input = False
    while not valid_input:
        choice = input("Choose an option: ")
        if choice in ["1", "2"]:
            valid_input = True
        else:
            print("Invalid input.")
    return choice

# Function to get user input for running
def get_running_input():
    valid_input = False
    while not valid_input:
        choice = input("Choose an option: ")
        if choice in ["1", "2"]:
            valid_input = True
        else:
            print("Invalid input.")
    return choice

# Function to get user input for inventory
def get_inventory_input():
    valid_input = False
    while not valid_input:
        choice = input("Choose an option: ")
        if choice in ["1", "2"]:
            valid_input = True
        else:
            print("Invalid input.")
    return choice

# Function to get user input for item
def get_item_input():
    valid_input = False
    while not valid_input:
        choice = input("Choose an option: ")
        if choice in ["1", "2", "3"]:
            valid_input = True
        else:
            print("Invalid input.")
    return choice

# Function to get user input for item
def get_item_input2():
    valid_input = False
    while not valid_input:
        choice = input("Choose an option: ")
        if choice in ["1", "2"]:
            valid_input = True
        else:
            print("Invalid input.")
    return choice

# Function to get user input for item
def get_item_input3():
    valid_input = False
    while not valid_input:
        choice = input("Choose an option: ")
        if choice in ["1", "2", "3", "4"]:
            valid_input = True
        else:
            print("Invalid input.")
    return choice

# Function to get user input for item
def get_item_input4():
    valid_input = False
    while not valid_input:
        choice = input("Choose an option: ")
        if choice in ["1", "2", "3", "4", "5"]:
            valid_input = True
        else:
            print("Invalid input.")
    return choice

# Function to get user input for item
def get_item_input5():
    valid_input = False
    while not valid_input:
        choice = input("Choose an option: ")
        if choice in ["1", "2", "3", "4", "5", "6"]:
            valid_input = True
        else:
            print("Invalid input.")
    return choice

# Function to get user input for item
def get_item_input6():
    valid_input = False
    while not valid_input:
        choice = input("Choose an option: ")
        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            valid_input = True
        else:
            print("Invalid input.")
    return choice

# Function to get user input for item
def get_item_input7():
    valid_input = False
    while not valid_input:
        choice = input("Choose an option: ")
        if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            valid_input = True
        else:
            print("Invalid input.")
    return choice

# Function to get user input for item
def get_item_input8():
    valid_input = False
    while not valid_input:
        choice = input("Choose an option: ")
        if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            valid_input = True
        else:
            print("Invalid input.")
    return choice

# Funtion to get some input
def get_some_input():
    valid_input = False
    while not valid_input:
        choice = input("Choose an option: ")
        if choice in ["1"]:
            valid_input = True
        else:
            print("Invalid input.")
    return choice

def main():
    print("Welcome to the dungeon!")
    character = create_character()
    enemy = create_enemy()

    while character.is_alive() and enemy.is_alive():
        print()
        print("You have encountered an enemy!")
        print()
        print("Your options are:")
        print_options()
        choice = get_input()
        if choice == "1":
            attack(character, enemy)
            attack(enemy, character)
            print_health(character)
            print_health(enemy)
        elif choice == "2":
            print("You have {} health.".format(character.health))
            print("Your options are:")
            print("1. Use potion")
            print("2. Use bandage")
            choice = get_healing_input()
            if choice == "1":
                if "Potion" in character.inventory:
                    character.health += 20
                    remove_item(character, "Potion")
                    print("You have used a potion.")
                    print("You have {} health.".format(character.health))
                else:
                    print("You do not have a potion.")
            elif choice == "2":
                if "Bandage" in character.inventory:
                    character.health += 10
                    remove_item(character, "Bandage")
                    print("You have used a bandage.")
                    print("You have {} health.".format(character.health))
                else:
                    print("You do not have a bandage.")
        elif choice == "3":
            print("Your options are:")
            print("1. Run away")
            print("2. Stay and fight")
            choice = get_running_input()
            if choice == "1":
                print("You have escaped!")
                break
            elif choice == "2":
                print("You have chosen to stay and fight!")
                attack(enemy, character)
                print_health(character)
                print_health(enemy)
        if enemy.health <= 0:
            print("You have defeated the enemy!")
            print("You have gained 1 potion and 1 bandage.")
            add_item(character, "Potion")
            add_item(character, "Bandage")
            print_inventory(character)
            print("Your options are:")
            print("1. Continue")
            print("2. Quit")
            choice = get_some_input()
            if choice == "1":
                enemy = create_enemy()
            elif choice == "2":
                break
        if character.health <= 0:
            print("You have died!")
            print("Game over!")
            break

main()


