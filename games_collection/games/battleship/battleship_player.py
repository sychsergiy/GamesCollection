from games_collection.games.battleship.battleship_field import BattleshipField
from games_collection.games.battleship.cell import Cell
from games_collection.games.battleship.gun import Gun
from games_collection.games.battleship.player import Player


class BattleshipPlayer(object):

    def __init__(self, player: Player):
        self.player = player
        self._battleship_game = None

    def _connect_to_game(self, battleship_game):
        self._battleship_game = battleship_game

    def locate_ship(self, cell: Cell, ship_size: int) -> bool:
        battlefield = self._battleship_game.get_player_battleship_field(self)
        return battlefield.locate_ship(cell, ship_size)

    def finish_ships_locating_step(self) -> bool:
        battlefield = self._battleship_game.get_player_battleship_field(self)
        return battlefield.finish_ships_locating()

    def ships_locating_step_finished(self) -> bool:
        battlefield = self._battleship_game.get_player_battleship_field(self)
        return battlefield.ships_locating_finished

    def shot(self, cell: Cell) -> Gun.ShotResultEnum:
        battleship_field = self._get_battleship_field()
        if not battleship_field.ships_locating_finished:
            raise Exception("Ships not located")
        opponent_battleship_field = self._get_opponent_battleship_field()
        if not opponent_battleship_field.ships_locating_finished:
            raise Exception("Opponent ships not located")
        shot_result = opponent_battleship_field.shot(cell)
        if shot_result == Gun.ShotResultEnum.SHIP_DESTROYED:
            is_game_over = opponent_battleship_field.all_ships_destroyed
            if is_game_over:
                raise Exception("Game over")
        return shot_result

    def get_battlefield_view(self) -> list:
        return self._get_battleship_field().get_battlefield_view(True)

    def get_opponent_battlefield_view(self) -> list:
        return self._get_opponent_battleship_field().get_battlefield_view(False)

    def _get_battleship_field(self):
        if not self._battleship_game:
            raise Exception("Not connected to game")
        return self._battleship_game.get_player_battleship_field(self)

    def _get_opponent_battleship_field(self) -> BattleshipField:
        if not self._battleship_game:
            raise Exception("Not connected to game")
        return self._battleship_game.get_opponent_battleship_field(self)
