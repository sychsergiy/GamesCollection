from games_collection.game_configuration import AbstractGameConfiguration
from games_collection.games.guess_number.guess_number import NumberToGuess
from games_collection.games.guess_number.guess_number_strategy import (
    RandomNumberUpdateStrategy
)


class GuessNumberConfiguration(AbstractGameConfiguration):
    def __init__(self, guess_times_to_win: int, number_to_guess: NumberToGuess):
        self.guess_times_to_win = guess_times_to_win
        self.number_to_guess: NumberToGuess = number_to_guess


twice_guess_configuration = GuessNumberConfiguration(
    2, NumberToGuess(RandomNumberUpdateStrategy(1, 3))
)

once_guess_configuration = GuessNumberConfiguration(
    1, NumberToGuess(RandomNumberUpdateStrategy(1, 3))
)
