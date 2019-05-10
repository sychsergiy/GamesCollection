import typing as t
import copy

from games_collection.game import AbstractGame


class GamesCollection(object):
    def __init__(self, games: t.List[AbstractGame]):
        self._games = games

    def list_games(self):
        games_titles = [game.title for game in self._games]
        return games_titles

    def choose_game(self, game_title: str) -> AbstractGame:
        for game in self._games:
            if game.title == game_title:
                return copy.copy(game)
