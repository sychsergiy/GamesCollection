from games_collection.actions_handler import (
    AbstractAction,
    AbstractActionResult,
    ActionsHandlerRegister,
)
from games_collection.match import PlayerVsPlayerMatch
from games_collection.player import Player
from games_collection.settings import AbstractGameSettings


class AbstractGame(object):
    title = None

    def __init__(
        self, match: PlayerVsPlayerMatch, settings: AbstractGameSettings
    ):
        self._match = match
        self._settings = settings
        self._actions_handler = ActionsHandlerRegister()
        self._register_actions_handlers()

    def send_action(self, action: AbstractAction) -> AbstractActionResult:
        return self._actions_handler.handle_action(action)

    def _register_actions_handlers(self):
        raise NotImplementedError

    def is_player_turn(self, player: Player) -> bool:
        return self._match.is_player_turn(player)

    def finish_current_player_turn(self):
        self._match.finish_current_player_turn()
