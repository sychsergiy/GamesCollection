import typing as t

from games_collection.game_configurator import AbstractGameConfigurator


class GamesCollection(object):
    def __init__(self):
        self._configurators_map: t.Dict[str, AbstractGameConfigurator] = {}

    def add_game(self, title: str, configurator: AbstractGameConfigurator):
        self._configurators_map[title] = configurator

    def list_games(self) -> t.List[str]:
        return list(self._configurators_map.keys())

    def choose_game(self, game_title: str) -> AbstractGameConfigurator:
        return self._configurators_map[game_title]
