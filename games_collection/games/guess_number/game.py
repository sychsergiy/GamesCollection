from games_collection.games.guess_number.action_handlers import (
    TryToGuessActionHandler
)
from games_collection.games.guess_number.actions import (
    TryToGuessAction
)

from games_collection.game import AbstractGame
from games_collection.game_data import AbstractGameData
from games_collection.player import Player
from games_collection.actions_handler import (
    ActionsHandlerRegister,
    ActionRegister,
)

from games_collection.games.guess_number.guess_number import NumberToGuess
from games_collection.games.guess_number.guess_number_strategy import (
    RandomNumberUpdateStrategy
)


class GuessNumberGame(AbstractGame):
    def register_actions_handlers(self):
        update_strategy = RandomNumberUpdateStrategy(1, 10)
        number_to_guess = NumberToGuess(update_strategy)

        try_to_guess_action_handler = TryToGuessActionHandler(
            self._match, self._settings, number_to_guess
        )

        action_register = ActionRegister(
            try_to_guess_action_handler.action_class,
            try_to_guess_action_handler
        )

        self.actions_handler.register(action_register)
