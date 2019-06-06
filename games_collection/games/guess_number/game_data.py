from games_collection.game_data import AbstractGameData
from games_collection.games.guess_number.settings import GuessNumberSettings
from games_collection.match import PlayerVsPlayerMatch


class GuessNumberGameData(AbstractGameData):
    def __init__(
            self, settings: GuessNumberSettings, match: PlayerVsPlayerMatch,
    ):
        self._settings = settings
        self._match = match
