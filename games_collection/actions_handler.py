import typing as t


class AbstractAction(object):
    pass


class AbstractActionResult(object):
    pass


class AbstractActionHandler(object):
    action_class = None

    def handle(self, action: AbstractAction) -> AbstractActionResult:
        if not isinstance(action, self.action_class):
            raise Exception(
                f"Expected action: {self.action_class}, got: {type(action)}"
            )


class ActionRegister(t.NamedTuple):
    action_class: AbstractAction
    action_handler: AbstractActionHandler


class ActionsHandlerRegister(object):
    def __init__(self: t.List[ActionRegister]):
        self._actions_handlers_map = {}

    def register(self, action_register: ActionRegister):
        # todo: warning the same action will be overwritten
        self._actions_handlers_map[
            action_register.action_class
        ] = action_register.action_handler

    def _get_action_handler(
        self, action: AbstractAction
    ) -> AbstractActionHandler:
        action_class = type(action)
        return self._actions_handlers_map[action_class]

    def _is_action_registered(self, action):
        action_class = type(action)
        return action_class in self._actions_handlers_map.keys()

    def handle_action(self, action: AbstractAction) -> AbstractActionResult:
        if not self._is_action_registered(action):
            raise Exception(f"not registered action: {type(action)}")
        handler = self._get_action_handler(action)
        return handler.handle(action)
