from battleship.battlefield import Battlefield
from battleship.gun import Gun
from battleship.game_mode import GameMode
from battleship.player import Player
from battleship.game import Game


def test_player_battlefield_ready_to_start():
    ship_size_count_map = {1: 2}
    game_mode = GameMode(Battlefield(4, 4), ship_size_count_map)
    game = Game(
        Player("first_player"),
        Player("second_player"),
        game_mode,
    )

    assert game.next_turn(1, 1) == Gun.ShotResultEnum.MISS
    print('\n')
    game.print_battlefields()

    assert game.next_turn(2, 2) == Gun.ShotResultEnum.MISS
    print('\n')
    game.print_battlefields()

