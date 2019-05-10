import typing as t

from games_collection.game import AbstractGame
from typing import Type, TypeVar

TGame = TypeVar("TGame", bound="AbstractGame")


class GamesCollection(object):
    def __init__(self, games: t.List[Type[TGame]]):
        self._games = games

    def list_games(self):
        games_titles = [game.title for game in self._games]
        return games_titles

    def choose_game(self, game_title: str) -> Type[TGame]:
        for game in self._games:
            if game.title == game_title:
                return game
