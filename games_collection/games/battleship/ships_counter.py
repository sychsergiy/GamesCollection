from games_collection.games.battleship.settings import BattleshipSettings


class ShipsCounter(object):
    def __init__(self, game_mode: BattleshipSettings):
        self._game_mode = game_mode
        self._ship_size_count_map = game_mode.ship_size_map.copy()

    def add_ship(self, ship_size: int):
        self._ship_size_count_map[ship_size] += 1

    def retrieve_ship(self, ship_size: int) -> bool:
        if self.ships_with_size_left(ship_size):
            self._ship_size_count_map[ship_size] -= 1
            return True
        return False

    def ships_with_size_left(self, ship_size: int):
        ships_left_count = self._ship_size_count_map[ship_size]
        return ships_left_count

    def is_all_ships_retrieved(self) -> bool:
        at_least_one_ship_left = any(self._ship_size_count_map.values())
        return not at_least_one_ship_left
