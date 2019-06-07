from games_collection.game_configurator import (
    AbstractGameConfigurator,
)
from games_collection.games.guess_number.configurations import (
    GuessNumberConfiguration
)
from games_collection.games.guess_number.game import GuessNumberGame
from games_collection.games.guess_number.settings import GuessNumberSettings
from games_collection.match import PlayerVsPlayerMatch


class GuessNumberConfigurator(AbstractGameConfigurator):
    def create_game_from_configuration(
            self,
            match: PlayerVsPlayerMatch,
            game_configuration: GuessNumberConfiguration
    ) -> GuessNumberGame:
        settings = GuessNumberSettings(game_configuration.guess_times_to_win)
        game = GuessNumberGame(
            match, settings, game_configuration.number_to_guess
        )
        return game
