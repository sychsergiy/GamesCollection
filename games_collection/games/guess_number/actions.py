from games_collection.player import Player


class AbstractAction(object):
    pass


class TryToGuessAction(AbstractAction):
    def __init__(self, player: Player, number: int):
        self.player = player
        self.number = number
