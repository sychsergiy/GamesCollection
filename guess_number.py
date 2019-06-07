import random

from games_collection.match import PlayerVsPlayerMatch
from games_collection.player import Player

from games_collection.games.guess_number.game import GuessNumberGame
from games_collection.games.guess_number.settings import GuessNumberSettings
from games_collection.games.guess_number.actions import TryToGuessAction


def get_random_number():
    return random.randint(1, 3)


def run_guess_number():
    player1 = Player("Player1", 1)
    player2 = Player("Player2", 2)
    match = PlayerVsPlayerMatch(player1, player2)
    settings = GuessNumberSettings(2)
    game = GuessNumberGame(match, settings)

    while True:
        result = game.send_action(
            TryToGuessAction(player1, get_random_number())
        )
        if result.guessed:
            print(f"Player: {player1} guess number")
        if result.left_to_guess == 0:
            print(f"Game over: {player1} win")
            break
        print(result.left_to_guess)
        result = game.send_action(
            TryToGuessAction(player2, get_random_number())
        )
        if result.left_to_guess == 0:
            print(f"Game over: {player2} win")
            break


if __name__ == "__main__":
    run_guess_number()
