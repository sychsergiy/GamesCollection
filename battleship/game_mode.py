import typing as t

from battleship.battlefield import Battlefield


class GameMode(t.NamedTuple):
    battlefield: Battlefield
    ship_size_map: dict


standard_game_mode = GameMode(
    Battlefield(8, 8), {1: 4, 2: 3, 3: 2, 4: 1}
)
