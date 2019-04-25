import typing as t

from battleship.game_mode import GameMode
from battleship.ship import Ship


class ShipsCounter(object):
    def __init__(self, game_mode: GameMode):
        self._game_mode = game_mode
        self._ship_size_count_map = game_mode.ship_size_map.copy()
        # todo: maybe save retrieved ships here and move ships_health management
        # todo: to this class

    def retrieve_ship(self, ship_size: int) -> t.Union[Ship, None]:
        ships_left_count = self._ship_size_count_map[ship_size]
        if ships_left_count > 0:
            self._ship_size_count_map[ship_size] -= 1
            return Ship(ship_size)

    def is_all_ships_retrieved(self) -> bool:
        at_least_one_ship_left = any(self._ship_size_count_map.values())
        return not at_least_one_ship_left
