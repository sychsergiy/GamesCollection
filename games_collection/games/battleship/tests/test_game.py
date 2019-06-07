import pytest

from games_collection.games.battleship.actions.finish_ships_locating import \
    FinishShipsLocatingAction
from games_collection.games.battleship.actions.locate_ship import \
    LocateShipAction
from games_collection.games.battleship.actions.shot import ShotAction
from games_collection.match import PlayerVsPlayerMatch
from games_collection.player import Player
from games_collection.games.battleship.battlefield import Battlefield
from games_collection.games.battleship.cell import Cell
from games_collection.games.battleship.gun import Gun
from games_collection.games.battleship.settings import BattleshipSettings
from games_collection.games.battleship.game.game import BattleshipGame
from games_collection.games.battleship.player.exceptions import (
    OpponentTurnException,
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

    assert player1.shot(Cell(0, 0)) == Gun.ShotResultEnum.SHIP_DESTROYED
    assert player2.shot(Cell(0, 0)) == Gun.ShotResultEnum.SHIP_DESTROYED

    with pytest.raises(OpponentTurnException):  # it is not your turn exception
        assert player2.shot(Cell(1, 0)) == Gun.ShotResultEnum.MISS


def test_new_game_using_actions():
    ship_size_count_map = {1: 2}
    game_mode = BattleshipSettings(Battlefield(4, 4), ship_size_count_map)

    p1 = Player("player1", 1)
    p2 = Player("player2", 2)
    match = PlayerVsPlayerMatch(p1, p2)
    game = BattleshipGame(match, game_mode)

    result = game.send_action(LocateShipAction(p1, Cell(0, 0), 1))
    assert result.located is True
    result = game.send_action(FinishShipsLocatingAction(p1))
    assert result.finished is False
    result = game.send_action(LocateShipAction(p1, Cell(3, 3), 1))
    assert result.located is True
    result = game.send_action(FinishShipsLocatingAction(p1))
    assert result.finished is True

    result = game.send_action(LocateShipAction(p2, Cell(0, 0), 1))
    assert result.located is True
    result = game.send_action(FinishShipsLocatingAction(p2))
    assert result.finished is False
    result = game.send_action(LocateShipAction(p2, Cell(3, 3), 1))
    assert result.located is True
    result = game.send_action(FinishShipsLocatingAction(p2))
    assert result.finished is True

    result = game.send_action(ShotAction(p1, Cell(0, 0)))
    assert result.shot_result == Gun.ShotResultEnum.SHIP_DESTROYED
    result = game.send_action(ShotAction(p2, Cell(0, 0)))
    assert result.shot_result == Gun.ShotResultEnum.SHIP_DESTROYED
    assert result.is_game_over is False

    with pytest.raises(OpponentTurnException):  # it is not your turn exception
        game.send_action(ShotAction(p2, Cell(0, 0)))
