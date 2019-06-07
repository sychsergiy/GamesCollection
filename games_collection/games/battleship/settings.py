from games_collection.games.battleship.battlefield import Battlefield
from games_collection.settings import AbstractGameSettings


class BattleshipSettings(AbstractGameSettings):
    def __init__(self, battlefield: Battlefield, ship_size_map: dict):
        self.battlefield = battlefield
        self.ship_size_map = ship_size_map


standard_match_settings = BattleshipSettings(
    Battlefield(8, 8), {1: 4, 2: 3, 3: 2, 4: 1}
)

short_match_settings = BattleshipSettings(Battlefield(8, 8), {2: 3})
