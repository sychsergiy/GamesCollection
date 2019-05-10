from games_collection.games.battleship.gun import Gun
from games_collection.games.battleship.cell import Cell
from games_collection.games.battleship.player import Player
from games_collection.games.battleship.game_mode import GameMode
from games_collection.games.battleship.player_battlefield import (
    PlayerBattlefield
)


class GameOverException(Exception):
    pass


class ShipsLocatingStepNotFinished(Exception):
    pass


class Game(object):
    def __init__(
            self,
            first_player: Player,
            second_player: Player,
            game_mode: GameMode,
    ):
        self._first_player_battlefield = PlayerBattlefield(
            first_player, game_mode
        )
        self._second_player_battlefield = PlayerBattlefield(
            second_player, game_mode
        )
        self._first_player_turn = False

    def first_player_locate_ship(self, x: int, y: int, ship_size) -> bool:
        cell = Cell(x, y)
        return self._locate_ship_on_player_battlefield(
            self._first_player_battlefield, cell, ship_size
        )

    def second_player_locate_ship(self, x: int, y: int, ship_size) -> bool:
        cell = Cell(x, y)
        return self._locate_ship_on_player_battlefield(
            self._second_player_battlefield, cell, ship_size
        )

    @staticmethod
    def _locate_ship_on_player_battlefield(
            player_battlefield: PlayerBattlefield,
            cell: Cell,
            ship_size: int
    ) -> bool:
        return player_battlefield.locate_ship(cell, ship_size)

    @property
    def first_player_finish_ships_locating_step(self) -> bool:
        return self.finish_ships_locating_step(self._first_player_battlefield)

    @property
    def second_player_finish_ships_locating_step(self) -> bool:
        return self.finish_ships_locating_step(self._second_player_battlefield)

    @staticmethod
    def finish_ships_locating_step(
            player_battlefield: PlayerBattlefield
    ) -> bool:
        return player_battlefield.finish_ships_locating()

    @property
    def ships_locating_step_finished(self) -> bool:
        return (
                self._first_player_battlefield.ships_locating_finished
                and self._second_player_battlefield.ships_locating_finished
        )

    def next_hit(self, x: int, y: int) -> Gun.ShotResultEnum:
        if not self.ships_locating_step_finished:
            raise ShipsLocatingStepNotFinished(
                "Ships locating step not finished"
            )

        cell = Cell(x, y)
        if self._first_player_turn:
            self._first_player_turn = not self._first_player_turn
            return self._player_battlefield_hit(self._first_player_battlefield,
                                                cell)
        else:
            self._first_player_turn = not self._first_player_turn
            return self._player_battlefield_hit(self._second_player_battlefield,
                                                cell)

    def get_current_turn_player_battlefield(self):
        if self._first_player_turn:
            return self._first_player_battlefield.get_battlefield_view(True)
        else:
            return self._second_player_battlefield.get_battlefield_view(True)

    def get_current_turn_player_opponent_battlefield(self):
        if self._first_player_turn:
            return self._first_player_battlefield.get_battlefield_view(False)
        else:
            return self._second_player_battlefield.get_battlefield_view(False)

    @staticmethod
    def _player_battlefield_hit(
            player_battlefield: PlayerBattlefield, cell: Cell
    ) -> Gun.ShotResultEnum:
        shot_result = player_battlefield.shot(cell)
        if shot_result == Gun.ShotResultEnum.SHIP_DESTROYED:
            # todo: handle game over
            is_game_over = player_battlefield.all_ships_destroyed
            if is_game_over:
                raise GameOverException(
                    f"Game over, {player_battlefield._player.name} winner"
                )
        return shot_result
