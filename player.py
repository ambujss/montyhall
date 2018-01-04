import random

NOCHANGE = "No Change"
CHANGE = "Change"

class _Player(object):
    """
    A Player that can play the monty hall game. The player is
    initialized with a strategy, CHANGE or NOCHANGE. With the CHANGE
    strategy, the player will always change their pick after the
    door with the goat is revelaed. With NOCHANGE, the player will
    always stick to its original selection.
    """
    def __init__(self):
        self.reset()

    def reset(self):
        self.selection = None
        self.bad_door = None

        self.selections = set([1,2,3])

    def initial_choice(self):
        self.selection = random.randint(1,3)
        self.selections.remove(self.selection)
        return self.selection

    def update_bad_door(self, bad_door):
        self.bad_door = bad_door
        self.selections.remove(bad_door)

    def second_choice(self):
        raise NotImplementedError("method second_choice not implemented")

class PlayerChange(_Player):
    def __init__(self):
        super(PlayerChange, self).__init__()

    def second_choice(self):
        return self.selections.pop()

class PlayerNoChange(_Player):
    def __init__(self):
        super(PlayerNoChange, self).__init__()

    def second_choice(self):
        return self.selection

def new(strategy):
    if strategy == NOCHANGE:
        return PlayerNoChange()
    elif strategy == CHANGE:
        return PlayerChange()
    else:
        raise ValueError("Invalid strategy %s provided"%strategy)
