from games_collection.game import AbstractGame
from games_collection.game_data import AbstractGameData
from games_collection.player import Player

from games_collection.games.guess_number.player import (
    GuessNumberPlayer
)


class GuessNumberGame(AbstractGame):
    def create_game_player(self, player: Player) -> GuessNumberPlayer:
        return GuessNumberPlayer(AbstractGameData())
