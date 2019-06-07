import typing as t

from games_collection.game import AbstractGame
from games_collection.match import PlayerVsPlayerMatch
from games_collection.game_configuration import AbstractGameConfiguration


class AbstractGameConfigurator(object):
    def __init__(self, configurations: t.List[AbstractGameConfiguration]):
        self._available_configurations = configurations

    def create_game_from_configuration(
            self,
            match: PlayerVsPlayerMatch,
            game_configuration: AbstractGameConfiguration
    ) -> AbstractGame:
        raise NotImplementedError

    def get_available_configurations(self) -> t.List[AbstractGameConfiguration]:
        return self._available_configurations
