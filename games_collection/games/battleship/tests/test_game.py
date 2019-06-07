import pytest

from games_collection.games.battleship.actions.finish_ships_locating import (
    FinishShipsLocatingAction,
)
from games_collection.games.battleship.actions.locate_ship import (
    LocateShipAction,
)
from games_collection.games.battleship.actions.shot import ShotAction
from games_collection.games.battleship.battlefield import Battlefield
from games_collection.games.battleship.cell import Cell
from games_collection.games.battleship.exceptions import OpponentTurnException
from games_collection.games.battleship.game import BattleshipGame
from games_collection.games.battleship.gun import Gun
from games_collection.games.battleship.settings import BattleshipSettings
from games_collection.match import PlayerVsPlayerMatch
from games_collection.player import Player


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
