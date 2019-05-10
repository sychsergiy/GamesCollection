from games_collection.games.battleship.player.player import BattleshipPlayer
from games_collection.games.battleship.game_mode import GameMode
from games_collection.games.battleship.battleship_field import (
    BattleshipField
)
from games_collection.game import AbstractGame
from games_collection.player import Player

from .exceptions import (
    GameNotFinishedException,
    PlayersAlreadyConnectedException,
    PlayerNotConnectedException,
)


class BattleshipGame(AbstractGame):
    title = "Battleship"

    def __init__(self, game_mode: GameMode):
        super(BattleshipGame, self).__init__()
        self._first_player = None
        self._second_player = None

        self._current_turn_player_id = None

        self._first_player_battlefield = BattleshipField(game_mode)
        self._second_player_battlefield = BattleshipField(game_mode)

        self._winner = None
        self._looser = None

    def is_player_turn(self, battleship_player: BattleshipPlayer):
        return self._current_turn_player_id == battleship_player.player.id

    def finish_current_player_turn(self):
        if self._current_turn_player_id == self._first_player.id:
            self._current_turn_player_id = self._second_player.id
        elif self._current_turn_player_id == self._second_player.id:
            self._current_turn_player_id = self._first_player.id

    def check_player_connected(self):
        if not self._first_player:
            raise PlayerNotConnectedException(
                "First player not connected"
            )
        if not self._second_player:
            raise PlayerNotConnectedException(
                "Second player not connected"
            )

    def get_player_battleship_field(
            self, battleship_player: BattleshipPlayer
    ) -> BattleshipField:
        self.check_player_connected()
        if battleship_player.player.id == self._first_player.id:
            return self._first_player_battlefield
        elif battleship_player.player.id == self._second_player.id:
            return self._second_player_battlefield

    def get_opponent_battleship_field(
            self, battleship_player: BattleshipPlayer
    ) -> BattleshipField:
        self.check_player_connected()
        if battleship_player.player.id == self._first_player.id:
            return self._first_player_battlefield
        elif battleship_player.player.id == self._second_player.id:
            return self._second_player_battlefield

    def connect_player(self, battleship_player: BattleshipPlayer):
        if not self._first_player:
            self._first_player = battleship_player.player
            self._current_turn_player_id = self._first_player.id
            battleship_player.connect_to_game(self)
        elif not self._second_player:
            self._second_player = battleship_player.player
            battleship_player.connect_to_game(self)
        else:
            raise PlayersAlreadyConnectedException(
                "Players already connected"
            )

    def get_result_info(self) -> dict:
        if not self.finished:
            raise GameNotFinishedException(
                "Game not finished, can't set winner"
            )
        result = {
            'winner': self._winner,
            'looser': self._looser,
        }
        return result

    @property
    def winner(self) -> Player:
        return self._winner

    @property
    def looser(self) -> Player:
        return self._looser

    def set_winner(self, battleship_player: BattleshipPlayer):
        self.check_player_connected()
        if not self.finished:
            raise Exception("Game not finished, can't set winner")

        if self._first_player.id == battleship_player.player.id:
            self._winner = self._first_player
            self._looser = self._second_player
        elif self._second_player.id == battleship_player.player.id:
            self._winner = self._second_player
            self._looser = self._second_player
