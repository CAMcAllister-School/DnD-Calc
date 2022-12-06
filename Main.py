"""Name: Andrew McAllister"""
# This is a die roller and calculator for Dungeons and Dragons 5th Edition
import random
# Definitely need to use random for dice rolling


def roll_advantage():
    """
    This function generates two random numbers from 1 to 20
    :return: The higher of the two numbers
    """
    func_roll1 = random.randint(1, 20)
    func_roll2 = random.randint(1, 20)
    if func_roll1 > func_roll2:
        func_roll = func_roll1
    else:
        func_roll = func_roll2
    return func_roll


def roll_disadvantage():
    """
    This function generates two random numbers from 1 to 20
    :return: The lower of the two numbers
    """
    func_roll1 = random.randint(1, 20)
    func_roll2 = random.randint(1, 20)
    if func_roll1 < func_roll2:
        func_roll = func_roll1
    else:
        func_roll = func_roll2
    return func_roll


def get_damage(amount, size):
    """
    This function generates a total of rolled dice of a single size
    :param amount: The amount of rolled dice
    :param size: The size of the dice
    :return: The total of the rolled dice
    """
    total = 0
    for x in range(amount):
        total += random.randint(1, size)
    return total


def attack():
    """
    This function asks the user for an AC and bonus to hit, as well as if the roll is with
    advantage or disadvantage, and determines if the roll succeeds or fails.
    :return: True if user wants to continue
    """
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
    except(TypeError, ValueError):
        print("Invalid command. Try again.\n")
        return True


def save():
    """
    This function asks the user for a DC and bonus to save, as well as if the roll is with
    advantage or disadvantage, and determines if the roll succeeds or fails.
    :return: True if user wants to continue
    """
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
    except(TypeError, ValueError):
        print("Invalid command. Try again.\n")
        return True


def damage():
    """
    This function asks the user for an amount of dice and the size of the dice, as well as a modifier, and
    outputs the total of the dice.
    :return: True if user wants to continue
    """
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
    except(TypeError, ValueError):
        print("Invalid command. Try again.\n")
        return True


def menu():
    """
    The purpose of this function is to direct the user to the attack, save, or damage function
    then loop when the function has been executed
    """
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


def main():
    """
    The purpose of this function is to introduce the program and then go to the menu
    """
    print("Hello! This is a dice roller and calculator for Dungeons and Dragons.")
    menu()


if __name__ == "__main__":
    main()
