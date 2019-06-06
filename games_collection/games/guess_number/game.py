from games_collection.game import AbstractGame
from games_collection.game_player import AbstractGamePlayer
from games_collection.player import Player


class GuessNumberGame(AbstractGame):
    def create_game_player(self, player: Player) -> AbstractGamePlayer:
        pass
