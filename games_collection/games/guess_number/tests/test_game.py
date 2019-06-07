import pytest

from games_collection.games.guess_number.actions import TryToGuessAction
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

    result = game.send_action(TryToGuessAction(player1, 1))
    assert result.guessed is False
    game.send_action(TryToGuessAction(player2, 1))

    with pytest.raises(Exception):
        game.send_action(TryToGuessAction(player2, 1))
