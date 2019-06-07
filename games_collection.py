from games_collection.games.battleship.configurations import (
    short_game_configuration,
    standard_configuration,
)
from games_collection.games.battleship.configurator import (
    BattleshipConfigurator,
)
from games_collection.games.guess_number.configurations import (
    once_guess_configuration,
    twice_guess_configuration,
)
from games_collection.games.guess_number.configurator import (
    GuessNumberConfigurator,
)
from games_collection.games_collection import GamesCollection
from games_collection.match import PlayerVsPlayerMatch
from games_collection.player import Player


def create_games_collection() -> GamesCollection:
    games_collection = GamesCollection()

    guess_number_configurator = GuessNumberConfigurator(
        [once_guess_configuration, twice_guess_configuration]
    )
    battleship_configurator = BattleshipConfigurator(
        [standard_configuration, short_game_configuration]
    )

    games_collection.add_game("guess_number", guess_number_configurator)
    games_collection.add_game("battleship", battleship_configurator)

    return games_collection


def run_games_collection_demo():
    games_collection = create_games_collection()
    print(games_collection.list_games())
    guess_number_configurator = games_collection.choose_game("guess_number")
    configurations = guess_number_configurator.get_available_configurations()
    configuration = configurations[0]

    match = PlayerVsPlayerMatch(Player("player1", 1), Player("player2", 2))
    guess_number_game = guess_number_configurator.create_game_from_configuration(
        match, configuration
    )
    print("guess_number game created")

    battleship_configurator = games_collection.choose_game("battleship")
    configurations = battleship_configurator.get_available_configurations()
    configuration = configurations[0]
    match = PlayerVsPlayerMatch(Player("player1", 1), Player("player2", 2))
    battleship_game = battleship_configurator.create_game_from_configuration(
        match, configuration
    )
    print("battleship game created")


if __name__ == "__main__":
    run_games_collection_demo()
