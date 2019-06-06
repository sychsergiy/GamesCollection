import typing as t

from games_collection.games.guess_number.counter import Counter
from games_collection.player import Player
from games_collection.games.guess_number.settings import GuessNumberSettings

counter = Counter()


class AbstractAction(object):
    pass


class TryToGuessAction(AbstractAction):
    def __init__(self, player: Player, number):
        self.player = player
        self.number = number


class ActionHandler(object):
    def handle(self, action: AbstractAction):
        raise NotImplementedError


class TryToGuessActionHandler(ActionHandler):
    _action_class = TryToGuessAction

    def __init__(self, settings: GuessNumberSettings):
        self._settings = settings

    def get_player_counter(self, player: Player) -> Counter:
        return counter

    def get_number_to_guess(self) -> int:
        return 1

    def update_number_to_guess(self):
        raise NotImplementedError

    def handle(self, action: TryToGuessAction):
        if not isinstance(action, self._action_class):
            raise Exception("Not Try To Guess action, can't be handled")
        player_counter = self.get_player_counter(action.player)
        if action.number == self.get_number_to_guess():
            player_counter.increment_guesses()
            self.update_number_to_guess()
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
