from games_collection.game_configuration import AbstractGameConfiguration


class BattleshipConfiguration(AbstractGameConfiguration):
    def __init__(
        self,
        battlefield_width: int,
        battlefield_height: int,
        ship_size_map: dict,
    ):
        self.battlefield_width: int = battlefield_width
        self.battlefield_height: int = battlefield_height
        self.ship_size_map = ship_size_map


standard_configuration = BattleshipConfiguration(8, 8, {1: 4, 2: 3, 3: 2, 4: 1})

short_game_configuration = BattleshipConfiguration(5, 5, {2: 3})
