from games_collection.games.battleship.battleship_field import BattleshipField
from games_collection.player import Player


class PlayersBattleshipFields(object):
    def __init__(self):
        self._players_battleship_fields_map = {}

    def add_player_battleship_field(
        self, player: Player, battleship_field: BattleshipField
    ):
        self._players_battleship_fields_map[player.id] = battleship_field

    def get_player_battleship_field(self, player: Player) -> BattleshipField:
        if player.id not in self._players_battleship_fields_map:
            raise Exception("Player not in battleship_fields map")
        return self._players_battleship_fields_map[player.id]

    def get_opponent_battleship_field(self, player: Player) -> BattleshipField:
        for key, value in self._players_battleship_fields_map.items():
            if key != player.id:
                return value
        raise Exception("No players found")
