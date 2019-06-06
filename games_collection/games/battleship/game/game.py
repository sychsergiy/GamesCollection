from games_collection.settings import AbstractGameSettings
from games_collection.games.battleship.game_mode import GameMode
from games_collection.games.battleship.battleship_field import BattleshipField
from games_collection.game import AbstractGame
from games_collection.match import PlayerVsPlayerMatch
from games_collection.player import Player


class BattleshipGame(AbstractGame):
    title = "Battleship"

    def __init__(self, match: PlayerVsPlayerMatch, game_mode: GameMode):
        # todo: Inherit game_mode from AbstractGameSettings
        super(BattleshipGame, self).__init__(match, AbstractGameSettings())
        self._game_mode = game_mode

        self._players_battleship_fields = {}

    def create_game_player(self, player: Player):
        if player not in (self._match.first_player, self._match.second_player):
            raise Exception("Player not in match")

        self._players_battleship_fields[player.id] = BattleshipField(
            self._game_mode
        )
        from games_collection.games.battleship.player.player import (
            BattleshipPlayer,
        )

        return BattleshipPlayer(player, self)

    def get_player_battleship_field(self, player: Player) -> BattleshipField:
        return self._players_battleship_fields.get(player.id)

    def get_opponent_battleship_field(self, player: Player) -> BattleshipField:
        for key, value in self._players_battleship_fields.items():
            if key != player.id:
                return value
        raise Exception("Opponent battleship ship field doesn't exists")
