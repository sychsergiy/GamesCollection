import typing as t

from games_collection.games.guess_number.action_handlers import ActionHandler
from games_collection.games.guess_number.actions import AbstractAction


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
