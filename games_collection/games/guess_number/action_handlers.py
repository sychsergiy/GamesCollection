from games_collection.games.guess_number.guess_number import NumberToGuess
from games_collection.games.guess_number.guesses_counter import GuessesCounter
from games_collection.games.guess_number.settings import GuessNumberSettings
from games_collection.games.guess_number.players_counters import PlayersCounters
from games_collection.games.guess_number.actions import (
    TryToGuessAction,
    TryToGuessActionResult,
)
from games_collection.match import PlayerVsPlayerMatch
from games_collection.player import Player
from games_collection.actions_handler import AbstractActionHandler


class TryToGuessActionHandler(AbstractActionHandler):
    action_class = TryToGuessAction

    def __init__(
        self,
        match: PlayerVsPlayerMatch,
        settings: GuessNumberSettings,
        number_to_guess: NumberToGuess,
    ):
        self._settings = settings
        self._number_to_guess = number_to_guess
        self._match = match

        self._players_counters = PlayersCounters()
        self._init_players_counters()

    def _init_players_counters(self):
        self._players_counters.add_player_counter(
            self._match.first_player, GuessesCounter()
        )
        self._players_counters.add_player_counter(
            self._match.second_player, GuessesCounter()
        )

    def get_player_counter(self, player: Player) -> GuessesCounter:
        return self._players_counters.get_player_counter(player)

    def handle(self, action: TryToGuessAction) -> TryToGuessActionResult:
        super(TryToGuessActionHandler, self).handle(action)
        if not self._match.is_player_turn(action.player):
            raise Exception(f"Not {action.player} turn now")

        player_counter = self.get_player_counter(action.player)
        if action.number == self._number_to_guess.get_number():
            player_counter.increment_guesses()
            self._number_to_guess.update()
        else:
            player_counter.increment_misses()
        self._match.finish_current_player_turn()
        left_to_guess = (
            self._settings.guess_times_to_winn - player_counter.guesses
        )
        action_result = TryToGuessActionResult(
            guessed=True,
            left_to_guess=left_to_guess,
            guessed_times=player_counter.guesses,
            missed_times=player_counter.misses,
        )
        return action_result
