from games_collection.games.guess_number.actions import (
    AbstractAction,
    TryToGuessAction,
)
from games_collection.games.guess_number.guess_number import NumberToGuess
from games_collection.games.guess_number.guesses_counter import GuessesCounter
from games_collection.games.guess_number.players_counters import (
    PlayersCounters
)
from games_collection.games.guess_number.settings import GuessNumberSettings
from games_collection.player import Player


class ActionHandler(object):
    _action_class = None

    def handle(self, action: AbstractAction):
        if not isinstance(action, self._action_class):
            raise Exception(
                f"Expected action: {self._action_class}, got: {type(action)}"
            )
        raise NotImplementedError


class TryToGuessActionHandler(ActionHandler):
    _action_class = TryToGuessAction

    def __init__(
            self,
            settings: GuessNumberSettings,
            players_counters: PlayersCounters,
            number_to_guess: NumberToGuess
    ):
        self._settings = settings
        self._players_counters_storage: PlayersCounters = players_counters
        self._number_to_guess = number_to_guess

    def get_player_counter(self, player: Player) -> GuessesCounter:
        return self._players_counters_storage.get_player_counter(player)

    def handle(self, action: TryToGuessAction):
        super(TryToGuessActionHandler, self).handle(action)
        player_counter = self.get_player_counter(action.player)
        if action.number == self._number_to_guess.get_number():
            player_counter.increment_guesses()
            self._number_to_guess.update()
        else:
            player_counter.increment_misses()
