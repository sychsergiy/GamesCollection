from games_collection.actions_handler import (
    AbstractAction,
    AbstractActionResult,
)
from games_collection.player import Player


class TryToGuessAction(AbstractAction):
    def __init__(self, player: Player, number: int):
        self.player = player
        self.number = number


class TryToGuessActionResult(AbstractActionResult):
    def __init__(
        self,
        guessed: bool,
        left_to_guess: int,
        guessed_times: int,
        missed_times: int,
    ):
        self.guessed = guessed
        self.left_to_guess = left_to_guess
        self.guessed_times = guessed_times
        self.missed_times = missed_times
