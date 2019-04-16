from battleship.battlefield import Battlefield
from battleship.ships_locator import (
    VerticalShipsLocator,
    HorizontalShipsLocator,
)
from battleship.ship import Ship


# todo: fix scanner checks only ships nearby, but ship can be too big to locate

def test_ships_horizontal_locator():
    battlefield = Battlefield(5, 5)
    horizontal_locator = HorizontalShipsLocator(battlefield)

    ship = Ship(2)
    first_ship_located = horizontal_locator.locate_ship(ship, 2, 2)
    assert first_ship_located
    ship = Ship(1)
    second_ship_located = horizontal_locator.locate_ship(ship, 3, 2)
    assert not second_ship_located


def test_vertical_ship_locator_true():
    battlefield = Battlefield(5, 5)
    vertical_locator = VerticalShipsLocator(battlefield)

    ship = Ship(2)
    first_ship_located = vertical_locator.locate_ship(ship, 2, 2)
    assert first_ship_located

    ship = Ship(1)
    second_ship_located = vertical_locator.locate_ship(ship, 2, 3)
    assert not second_ship_located
