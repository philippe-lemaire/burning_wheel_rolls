import random


def roll(
    shade="black", dice=0, obstacle=None, open_ended=False, luck=False, last_roll=None
):
    """Rolls a Burning wheel test. Prints the outcome in plain English and returns a list of dice face values.
    Use the returned list as last_roll argument with luck=True to reroll with the Luck rule of artha spending"""
    # shade setting
    if shade.lower().startswith("b"):
        threshold = 4
    elif shade.lower().startswith("g"):
        threshold = 3
    elif shade.lower().startswith("w"):
        threshold = 2
    else:
        raise ValueError(
            "Shade must be a string such as 'b', 'black', 'grey', 'G', or 'white', 'w'"
        )

    # if luck, it's a reroll for exploding 6s
    if luck:
        rolls = last_roll
    else:
        rolls = [random.randint(1, 6) for die in range(dice)]

    # if the test is naturally open ended, or if it's a luck reroll
    if open_ended or luck:
        to_explode = rolls.count(6)
        # explode 6s
        while to_explode > 0:
            print("explosion")
            new_rolls = [random.randint(1, 6) for die in range(to_explode)]
            to_explode = new_rolls.count(6)
            rolls.extend(new_rolls)

    # Print the dice results
    print(f"You rolled: {rolls}.")
    successes = len([die for die in rolls if die >= threshold])

    if obstacle:
        if successes < obstacle:
            result = f"You failed to meet the obstacle. The obstacle was {obstacle} and you got {successes} successes."

        elif successes == obstacle:
            result = f"You met the obstacle. The obstacle was {obstacle} and you got {successes} successes."

        else:
            result = f"You beat the obstacle. The obstacle was {obstacle} and you got {successes} successes. Your margin of success is {successes-obstacle}."

    else:
        result = f"You got {successes} successes."

    return rolls, result
