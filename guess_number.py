import random

from games_collection.games.guess_number.guess_number import NumberToGuess
from games_collection.games.guess_number.guess_number_strategy import \
    RandomNumberUpdateStrategy
from games_collection.match import PlayerVsPlayerMatch
from games_collection.player import Player

from games_collection.games.guess_number.game import GuessNumberGame
from games_collection.games.guess_number.settings import GuessNumberSettings
from games_collection.games.guess_number.actions import TryToGuessAction


def get_random_number():
    return random.randint(1, 3)


def run_guess_number_demo():
    player1 = Player("Player1", 1)
    player2 = Player("Player2", 2)
    match = PlayerVsPlayerMatch(player1, player2)
    settings = GuessNumberSettings(2)
    number_to_guess = NumberToGuess(RandomNumberUpdateStrategy(1, 3))
    game = GuessNumberGame(match, settings, number_to_guess)

    while True:
        result = game.send_action(
            TryToGuessAction(player1, get_random_number())
        )
        if result.guessed:
            print(f"{str(player1)} guess number")
        if result.left_to_guess == 0:
            print(f"Game over: {player1} win")
            break
        print(f"{str(player1)}: left to guess: {result.left_to_guess}")
        result = game.send_action(
            TryToGuessAction(player2, get_random_number())
        )
        if result.guessed:
            print(f"{str(player2)} guess number")
        if result.left_to_guess == 0:
            print(f"Game over: {player1} win")
            break
        print(f"{str(player2)}: left to guess: {result.left_to_guess}")


if __name__ == "__main__":
    run_guess_number_demo()
