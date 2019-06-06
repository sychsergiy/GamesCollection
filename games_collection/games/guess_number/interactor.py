import typing as t
import random

from games_collection.games.guess_number.settings import GuessNumberSettings
from games_collection.games.guess_number.counter import Counter
from games_collection.player import Player


class PlayersCountersStorage(object):
    def __init__(self):
        self.players_counters_map = {}

    def add_player_counter(self, player: Player, counter: Counter):
        self.players_counters_map[player.id] = counter

    def get_player_counter(self, player: Player) -> Counter:
        # todo: handle player.id not in players_counter_map
        return self.players_counters_map[player.id]


class AbstractNumberUpdateStrategy(object):
    def get_number(self) -> int:
        raise NotImplementedError


class RandomNumberUpdateStrategy(AbstractNumberUpdateStrategy):
    def __init__(self, min_value: int, max_value: int):
        self._min_value = min_value
        self._max_value = max_value

    def get_number(self) -> int:
        return random.randint(self._min_value, self._max_value)


class NumberToGuess(object):
    def __init__(
            self,
            update_strategy: AbstractNumberUpdateStrategy,
            initial_value: int = None,
    ):
        self._update_strategy = update_strategy
        self._current_number = (
            update_strategy.get_number()
            if initial_value is None else initial_value
        )

    def update(self):
        self._current_number = self._update_strategy.get_number()

    def get_number(self) -> int:
        return self._current_number


class AbstractAction(object):
    pass


class TryToGuessAction(AbstractAction):
    def __init__(self, player: Player, number):
        self.player = player
        self.number = number


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
            players_counters_storage: PlayersCountersStorage,
            number_to_guess: NumberToGuess
    ):
        self._settings = settings
        self._players_counters_storage: PlayersCountersStorage = \
            players_counters_storage
        self._number_to_guess = number_to_guess

    def get_player_counter(self, player: Player) -> Counter:
        return self._players_counters_storage.get_player_counter(player)

    def handle(self, action: TryToGuessAction):
        super(TryToGuessActionHandler, self).handle(action)
        player_counter = self.get_player_counter(action.player)
        if action.number == self._number_to_guess.get_number():
            player_counter.increment_guesses()
            self._number_to_guess.update()
        else:
            player_counter.increment_misses()


class ActionRegister(t.NamedTuple):
    action_class: t.ClassVar[AbstractAction]
    action_handler: ActionHandler


class ActionsHandler(object):
    def __init__(self: t.List[ActionRegister]):
        self._actions_handlers_map = {}

    def register(self, action_register: ActionRegister):
        # todo: warning the same action will be overwritten
        self._actions_handlers_map[action_register.action_class] = \
            action_register.action_handler

    def _get_action_handler(self, action: AbstractAction) -> ActionHandler:
        action_class = type(action)
        return self._actions_handlers_map[action_class]

    def _is_action_registered(self, action):
        action_class = type(action)
        return action_class not in self._actions_handlers_map.keys()

    def handle_action(self, action: AbstractAction):
        if not self._is_action_registered(action):
            raise Exception(f"not registred action: {type(action)}")
        handler = self._get_action_handler(action)
        handler.handle(action)
