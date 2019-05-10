import pytest

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

    with pytest.raises(Exception):
        game.next_hit(0, 0)
    assert game.first_player_finish_ships_locating_step == False
    assert game.first_player_locate_ship(0, 0, 1) == True
    assert game.first_player_locate_ship(3, 3, 1) == True
    assert game.first_player_finish_ships_locating_step == True

    with pytest.raises(Exception):
        game.next_hit(0, 0)
    assert game.second_player_finish_ships_locating_step == False
    assert game.second_player_locate_ship(0, 0, 1) == True
    assert game.second_player_locate_ship(3, 3, 1) == True
    assert game.second_player_finish_ships_locating_step == True

    assert game.next_hit(0, 0) == Gun.ShotResultEnum.SHIP_DESTROYED
    assert game.next_hit(0, 0) == Gun.ShotResultEnum.SHIP_DESTROYED

    assert game.next_hit(2, 2) == Gun.ShotResultEnum.MISS

    with pytest.raises(Exception):
        assert game.next_hit(3, 3)
