from games_collection.match import PlayerVsPlayerMatch
from games_collection.game_player import AbstractGamePlayer
from games_collection.player import Player
from games_collection.settings import AbstractGameSettings
from games_collection.actions_handler import ActionsHandlerRegister


class AbstractGame(object):
    title = None

    def __init__(
            self, match: PlayerVsPlayerMatch, settings: AbstractGameSettings
    ):
        self._match = match
        self._settings = settings
        self.actions_handler = ActionsHandlerRegister()

    def register_actions_handlers(self):
        raise NotImplementedError

    def is_player_turn(self, player: Player) -> bool:
        return self._match.is_player_turn(player)

    def finish_current_player_turn(self):
        self._match.finish_current_player_turn()

    def create_game_player(self, player: Player) -> AbstractGamePlayer:
        raise NotImplementedError
