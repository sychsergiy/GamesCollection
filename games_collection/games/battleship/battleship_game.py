from games_collection.games.battleship.battleship_player import BattleshipPlayer
from games_collection.games.battleship.game_mode import GameMode
from games_collection.games.battleship.battleship_field import (
    BattleshipField
)


class BattleshipGame(object):
    def __init__(self, game_mode: GameMode):
        self._first_player_id = None
        self._second_player_id = None

        self._current_turn_player_id = None

        self._first_player_battlefield = BattleshipField(game_mode)
        self._second_player_battlefield = BattleshipField(game_mode)

    def check_player_connected(self):
        if not self._first_player_id:
            raise Exception("First player not connected")
        if not self._second_player_id:
            raise Exception("Second player not connected")

    def get_player_battleship_field(
            self, battleship_player: BattleshipPlayer
    ) -> BattleshipField:
        self.check_player_connected()
        if battleship_player.player.id == self._first_player_id:
            return self._first_player_battlefield
        elif battleship_player.player.id == self._second_player_id:
            return self._second_player_battlefield

    def get_opponent_battleship_field(
            self, battleship_player: BattleshipPlayer
    ) -> BattleshipField:
        self.check_player_connected()
        if battleship_player.player.id == self._first_player_id:
            return self._first_player_battlefield
        elif battleship_player.player.id == self._second_player_id:
            return self._second_player_battlefield

    def connect_player(self, battleship_player: BattleshipPlayer):
        if not self._first_player_id:
            # todo: change name on unique field
            self._first_player_id = battleship_player.player.id
            battleship_player._connect_to_game(self)
        elif not self._second_player_id:
            self._second_player_id = battleship_player.player.id
            battleship_player._connect_to_game(self)
        else:
            raise Exception("Players already connected")
