import random

class Dice:
    """Represents a dice"""
    def __init__(self, side_number):
        self.side_number = side_number

    def roll(self):
        return random.randint(1, self.side_number)

class Roller:
    """Represents a dice reserve"""
    def __init__(self, sides: set[int]):
        self.dices_types = {x: Dice(x) for x in sides}

    def dice_roll(self, dice: int, number_of_dices=1):
        return [self.dices_types[dice].roll() for _ in range(number_of_dices)]

roller = Roller({3, 4, 6, 8, 12, 20, 100})

print(f'Roll 3d100: {roller.dice_roll(100, 3)}')
print(f'Roll 1d6: {roller.dice_roll(6)}')