from games_collection.games.guess_number.game import GuessNumberGame
from games_collection.games.guess_number.settings import GuessNumberSettings
from games_collection.match import PlayerVsPlayerMatch
from games_collection.player import Player


def test_game():
    player1 = Player("player1", 1)
    player2 = Player("player2", 2)
    match = PlayerVsPlayerMatch(player1, player2)

    settings = GuessNumberSettings(2)
    game = GuessNumberGame(match, settings)

    player1 = game.create_game_player(player1)

    assert player1.turn(1) is True
    assert player1.turn(-1) is False
