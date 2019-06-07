from games_collection.game_configurator import (
    AbstractGameConfigurator,
)
from games_collection.games.battleship.battlefield import Battlefield
from games_collection.games.battleship.battleship_field import BattleshipField
from games_collection.games.battleship.configurations import (
    BattleshipConfiguration
)
from games_collection.games.battleship.game import BattleshipGame
from games_collection.games.battleship.players_battleship_fields import (
    PlayersBattleshipFields
)
from games_collection.games.battleship.settings import BattleshipSettings

from games_collection.match import PlayerVsPlayerMatch


class BattleshipConfigurator(AbstractGameConfigurator):
    def create_game_from_configuration(
            self,
            match: PlayerVsPlayerMatch,
            configuration: BattleshipConfiguration
    ) -> BattleshipGame:
        settings = BattleshipSettings(
            Battlefield(
                configuration.battlefield_width,
                configuration.battlefield_height
            ),
            configuration.ship_size_map
        )
        players_battleship_fields = PlayersBattleshipFields()
        players_battleship_fields.add_player_battleship_field(
            match.first_player, BattleshipField(settings)
        )
        players_battleship_fields.add_player_battleship_field(
            match.second_player, BattleshipField(settings)
        )

        game = BattleshipGame(
            match, settings, players_battleship_fields
        )
        return game
