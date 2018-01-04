import random

GOAT = 0
GOLD = 1

class Door(object):
    """
    Object to simulate a door in the monty hall game
    """
    def __init__(self, value):
        self.value = value

class MontyHall(object):
    """
    One instance of the monty hall game. Generates 3 doors and randomly
    assigns 2 doors to the value GOAT and one to GOLD.
    """
    def __init__(self):
        self.doors = [Door(GOAT), Door(GOAT),
                      Door(GOLD)]
        random.shuffle(self.doors)
        self.selection = None

    def find_door(self, value, exclude_selection=True):
        """
        Find a door that has the provided value. Exclude the
        current selection if exclude_selection is True.
        """
        for i, door in enumerate(self.doors):
            doornum = i+1
            if exclude_selection and self.selection == doornum:
                continue
            if door.value == value:
                return doornum

    def play(self, player):
        """
        Play the game with the given player.
        """
        self.selection = player.initial_choice()
        bad_door = self.find_door(GOAT)
        player.update_bad_door(bad_door)
        new_selection = player.second_choice()

        final_door = self.doors[new_selection-1]

        # Player wins if their final door selection has GOLD behind it.
        return final_door.value == GOLD

def play_a_game(player):
    """
    game(player) palys one instance of the monty
    hall game with the given player
    """
    mh = MontyHall()
    return mh.play(player)
