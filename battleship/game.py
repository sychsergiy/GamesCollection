from battleship.player import Player
from battleship.game_mode import GameMode
from battleship.player_battlefield import PlayerBattlefield


class Game(object):
    def __init__(
            self,
            first_player: Player,
            second_player: Player,
            game_mode: GameMode,
    ):
        self._first_player_battlefield = PlayerBattlefield(first_player,
                                                           game_mode)
        self._second_player = PlayerBattlefield(second_player, game_mode)
