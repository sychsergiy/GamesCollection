import pytest

from games_collection.match import PlayerVsPlayerMatch
from games_collection.player import Player
from games_collection.games.battleship.battlefield import Battlefield
from games_collection.games.battleship.cell import Cell
from games_collection.games.battleship.gun import Gun
from games_collection.games.battleship.settings import BattleshipSettings
from games_collection.games.battleship.game.game import BattleshipGame
from games_collection.games.battleship.player.player import BattleshipPlayer
from games_collection.games.battleship.player.exceptions import (
    GameOverException,
    OpponentTurnException,
)
from games_collection.games.battleship.game.exceptions import (
    GameNotFinishedException,
    PlayersAlreadyConnectedException,
)


def test_player_battlefield_ready_to_start():
    ship_size_count_map = {1: 2}
    game_mode = BattleshipSettings(Battlefield(4, 4), ship_size_count_map)

    p1 = Player("player1", 1)
    p2 = Player("player2", 2)
    match = PlayerVsPlayerMatch(p1, p2)
    game = BattleshipGame(match, game_mode)

    player1 = game.create_game_player(p1)
    player2 = game.create_game_player(p2)

    assert player1.locate_ship(Cell(0, 0), 1) == True
    assert player1.finish_ships_locating_step() == False
    assert player1.ships_locating_step_finished() == False
    assert player1.locate_ship(Cell(3, 3), 1) == True
    assert player1.finish_ships_locating_step() == True
    assert player1.ships_locating_step_finished() == True

    assert player2.locate_ship(Cell(0, 0), 1) == True
    assert player2.finish_ships_locating_step() == False
    assert player2.ships_locating_step_finished() == False
    assert player2.locate_ship(Cell(3, 3), 1) == True
    assert player2.finish_ships_locating_step() == True
    assert player2.ships_locating_step_finished() == True

    # with pytest.raises(GameNotFinishedException):
    #     game.get_result_info()

    assert player1.shot(Cell(0, 0)) == Gun.ShotResultEnum.SHIP_DESTROYED
    assert player2.shot(Cell(0, 0)) == Gun.ShotResultEnum.SHIP_DESTROYED

    with pytest.raises(OpponentTurnException):  # it is not your turn exception
        assert player2.shot(Cell(1, 0)) == Gun.ShotResultEnum.MISS

    with pytest.raises(GameOverException):  # game over exception
        assert player1.shot(Cell(3, 3)) == Gun.ShotResultEnum.SHIP_DESTROYED

    # assert game.winner == player1.player
    # assert game.looser == player2.player
    #
    # expected_result = {"winner": player1.player, "looser": player2.player}
    # assert expected_result == game.get_result_info()
