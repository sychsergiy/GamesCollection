from games_collection.match import PlayerVsPlayerMatch
from games_collection.player import Player


class AbstractGame(object):
    title = None

    def __init__(self, match: PlayerVsPlayerMatch):
        self._match = match
        self._finished = False

    def finish(self):
        self._finished = True

    @property
    def finished(self):
        return self._finished

    def is_player_turn(self, player: Player) -> bool:
        return self._match.is_player_turn(player)

    def finish_current_player_turn(self):
        self._match.finish_current_player_turn()
