from games_collection.game_data import AbstractGameData


class AbstractGamePlayer(object):
    def __init__(self, game_data: AbstractGameData):
        self._game_data = game_data
