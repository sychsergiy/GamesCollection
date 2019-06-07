from games_collection.games.guess_number.guess_number_strategy import (
    AbstractNumberUpdateStrategy,
)


class NumberToGuess(object):
    def __init__(
        self,
        update_strategy: AbstractNumberUpdateStrategy,
        initial_value: int = None,
    ):
        self._update_strategy = update_strategy
        self._current_number = (
            update_strategy.get_number()
            if initial_value is None
            else initial_value
        )

    def update(self):
        self._current_number = self._update_strategy.get_number()

    def get_number(self) -> int:
        return self._current_number
