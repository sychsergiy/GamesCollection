from battleship.gun import Gun
from battleship.player import Player
from battleship.game_mode import GameMode
from battleship.player_battlefield import PlayerBattlefield


class Game(object):
    def __init__(
            self,
            first_player: Player,
            second_player: Player,
            game_mode: GameMode,
    ):
        self._first_player_battlefield = PlayerBattlefield(
            first_player, game_mode
        )
        self._second_player_battlefield = PlayerBattlefield(
            second_player, game_mode
        )
        self._first_player_turn = False

    def next_turn(self, x: int, y: int):
        if self._first_player_turn:
            self._first_player_turn = not self._first_player_turn
            return self._player_turn(self._first_player_battlefield, x, y)
        else:
            self._first_player_turn = not self._first_player_turn
            return self._player_turn(self._second_player_battlefield, x, y)

    def print_battlefields(self):
        # todo: get matrix and return
        if self._first_player_turn:
            self._first_player_battlefield.print_battlefield_view(True)
            print('')
            self._second_player_battlefield.print_battlefield_view(False)
        else:
            self._second_player_battlefield.print_battlefield_view(True)
            print('')
            self._first_player_battlefield.print_battlefield_view(False)

    def _player_turn(
            self,
            player_battlefield: PlayerBattlefield,
            x: int,
            y: int,
    ):
        shot_result = player_battlefield.shot(x, y)
        if shot_result == Gun.ShotResultEnum.SHIP_DESTROYED:
            # todo: handle game over
            is_game_over = player_battlefield.is_all_ships_destroyed()
            if is_game_over:
                raise Exception(
                    f"Game over, {player_battlefield._player.name} winner"
                )
        return shot_result
