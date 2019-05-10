from games_collection.player import Player
from games_collection.games.battleship.battleship_field import BattleshipField
from games_collection.games.battleship.cell import Cell
from games_collection.games.battleship.gun import Gun
from .exceptions import (
    OpponentNotConnectedToGameException,
    OpponentShipsNotLocatedException,
    PlayerNotConnectedToGameException,
    PlayerShipsNotLocatedException,
    OpponentTurnException,
    GameOverException
)


class BattleshipPlayer(object):

    def __init__(self, player: Player):
        self.player = player
        self._battleship_game = None

    def connect_to_game(self, battleship_game):
        if not self._battleship_game:
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
            raise PlayerShipsNotLocatedException("Player ships not located")
        opponent_battleship_field = self._get_opponent_battleship_field()
        if not opponent_battleship_field.ships_locating_finished:
            raise OpponentShipsNotLocatedException("Opponent ships not located")
        if not self.is_your_turn():
            raise OpponentTurnException("It is opponent turn now")
        self._battleship_game.finish_current_player_turn()

        shot_result = opponent_battleship_field.shot(cell)
        if shot_result == Gun.ShotResultEnum.SHIP_DESTROYED:
            is_game_over = opponent_battleship_field.all_ships_destroyed
            if is_game_over:
                self._battleship_game.finish()
                self._battleship_game.set_winner(self)
                raise GameOverException("Game over, you win!")

        return shot_result

    def is_your_turn(self):
        return self._battleship_game.is_player_turn(self)

    def get_battlefield_view(self) -> list:
        return self._get_battleship_field().get_battlefield_view(True)

    def get_opponent_battlefield_view(self) -> list:
        return self._get_opponent_battleship_field().get_battlefield_view(False)

    def _get_battleship_field(self):
        if not self._battleship_game:
            raise PlayerNotConnectedToGameException(
                "Player not connected to game"
            )
        return self._battleship_game.get_player_battleship_field(self)

    def _get_opponent_battleship_field(self) -> BattleshipField:
        if not self._battleship_game:
            raise OpponentNotConnectedToGameException(
                "Opponent not connected to game"
            )
        return self._battleship_game.get_opponent_battleship_field(self)
