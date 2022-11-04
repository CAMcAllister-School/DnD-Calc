# Name: Andrew McAllister
# This is a die roller and calculator for Dungeons and Dragons 5th Edition
import random
# Definitely need to use random for dice rolling


def roll_advantage():
    func_roll1 = random.randint(1, 20)
    func_roll2 = random.randint(1, 20)
    if func_roll1 > func_roll2:
        func_roll = func_roll1
    else:
        func_roll = func_roll2
    return func_roll
# This function rolls two d20s and takes the higher result


def roll_disadvantage():
    func_roll1 = random.randint(1, 20)
    func_roll2 = random.randint(1, 20)
    if func_roll1 < func_roll2:
        func_roll = func_roll1
    else:
        func_roll = func_roll2
    return func_roll
# This function rolls two d20s and takes the lower result


def get_damage(amount, size):
    total = 0
    for x in range(amount):
        total += random.randint(1, size)
    return total
# This function rolls an 'amount' of dice of one 'size' and totals them


def attack():
    try:
        attack_roll = None
        ac = int(input("Enemy Armor Class?\n"))
        pointer = input("Advantage or Disadvantage?\nInput 'Adv' 'Dis' or 'No'\n")
        modifier = int(input("Modifier?\n"))
        if pointer == "Adv":
            attack_roll = roll_advantage() + modifier
        elif pointer == "Dis":
            attack_roll = roll_disadvantage() + modifier
        elif pointer == "No":
            attack_roll = random.randint(1, 20) + modifier
        else:
            print("Invalid command. Try again.\n")
        if attack_roll == 20:
            print("You critically hit!\n")
        elif attack_roll == 1:
            print("You critically miss!\n")
        elif attack_roll >= ac:
            print("You hit with a total of", attack_roll, end=".\n")
        elif attack_roll < ac:
            print("You miss with a total of", attack_roll, end=".\n")
        internal_iterate = input("Anything else?\nInput 'Y' to continue.\n")
        if internal_iterate == "Y":
            return True
        else:
            return False
    except:
        print("Invalid command. Try again.\n")
        return True
# This function executes if the user wants to attack, and loops if the user wants to use the calculator again


def save():
    try:
        save_roll = None
        dc = int(input("Enemy Save DC?\n"))
        pointer = input("Advantage or Disadvantage?\nInput 'Adv' 'Dis' or 'No'\n")
        modifier = int(input("Modifier?\n"))
        if pointer == "Adv":
            save_roll = roll_advantage() + modifier
        elif pointer == "Dis":
            save_roll = roll_disadvantage() + modifier
        elif pointer == "No":
            save_roll = random.randint(1, 20) + modifier
        else:
            print("Invalid command. Try again.\n")
        if save_roll >= dc:
            print("You succeed with a total of", save_roll, end=".\n")
        elif save_roll < dc:
            print("You fail with a total of", save_roll, end=".\n")
        internal_iterate = input("Anything else?\nInput 'Y' to continue.\n")
        if internal_iterate == "Y":
            return True
        else:
            return False
    except:
        print("Invalid command. Try again.\n")
        return True
# This function executes if the user wants to roll a saving throw


def damage():
    try:
        d_amount = int(input("How many dice?\n"))
        d_size = int(input("What die size?\nInput 4, 6, 8, 10, or 12\n"))
        modifier = int(input("Modifier?\n"))
        all_damage = get_damage(d_amount, d_size) + modifier
        print("You deal", all_damage, "damage.\n")
        internal_iterate = input("Anything else?\nInput 'Y' to continue.\n")
        if internal_iterate == "Y":
            return True
        else:
            return False
    except:
        print("Invalid command. Try again.\n")
        return True
# This function executes if the user wants to roll damage


def menu():
    iterate = True
    while iterate:
        pointer = input("Attack, Save, or Damage?\nInput 'A' 'S' or 'D'\n")
        if pointer == "A":
            iterate = attack()
        elif pointer == "S":
            iterate = save()
        elif pointer == "D":
            iterate = damage()
        else:
            print("Invalid command. Try again.\n")
# This is the main menu function, which the program goes to after each attack roll, damage roll, or saving throw


def main():
    print("Hello! This is a dice roller and calculator for Dungeons and Dragons.")
    menu()


main()
