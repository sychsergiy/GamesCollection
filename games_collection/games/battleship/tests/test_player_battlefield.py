from games_collection.games.battleship.battleship_field import BattleshipField
from games_collection.games.battleship.cell import Cell
from games_collection.games.battleship.battlefield import Battlefield
from games_collection.games.battleship.settings import BattleshipSettings


def test_player_battlefield_not_ready_to_start():
    ship_size_count_map = {1: 4, 2: 2}
    game_mode = BattleshipSettings(Battlefield(4, 4), ship_size_count_map)

    p_b = BattleshipField(game_mode)
    cell = Cell(0, 0)
    assert p_b.locate_ship(cell, ship_size=1) == True
    assert p_b.locate_ship(cell, ship_size=1) == False
    assert p_b._ships_counter._ship_size_count_map[1] == 3

    assert p_b.ships_locating_finished == False
    assert p_b.finish_ships_locating() == False
    assert p_b.ships_locating_finished == False


def test_player_battlefield_ready_to_start():
    ship_size_count_map = {1: 2}
    game_mode = BattleshipSettings(Battlefield(4, 4), ship_size_count_map)

    p_b = BattleshipField(game_mode)
    assert p_b.locate_ship(Cell(0, 0), ship_size=1) == True
    assert p_b.locate_ship(Cell(3, 3), ship_size=1) == True
    assert p_b.locate_ship(Cell(0, 1), ship_size=1) == False
    assert p_b._ships_counter._ship_size_count_map[1] == 0

    assert p_b.ships_locating_finished == False
    assert p_b.finish_ships_locating() == True
    assert p_b.ships_locating_finished == True
