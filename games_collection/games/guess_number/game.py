from games_collection.games.guess_number.action_handlers import (
    TryToGuessActionHandler,
)
from games_collection.game import AbstractGame
from games_collection.actions_handler import ActionRegister

from games_collection.games.guess_number.guess_number import NumberToGuess
from games_collection.games.guess_number.settings import GuessNumberSettings
from games_collection.match import PlayerVsPlayerMatch


class GuessNumberGame(AbstractGame):
    def __init__(
            self, match: PlayerVsPlayerMatch,
            settings: GuessNumberSettings,
            number_to_guess: NumberToGuess
    ):
        self._number_to_guess = number_to_guess
        super(GuessNumberGame, self).__init__(match, settings)

    def _register_actions_handlers(self):
        try_to_guess_action_handler = TryToGuessActionHandler(
            self._match, self._settings, self._number_to_guess
        )

        action_register = ActionRegister(
            try_to_guess_action_handler.action_class,
            try_to_guess_action_handler,
        )

        self._actions_handler.register(action_register)
