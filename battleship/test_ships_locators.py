import pytest

from battleship.battlefield import Battlefield
from battleship.ships_locator import (
    VerticalShipLocator,
    HorizontalShipLocator,
)
from battleship.ship import Ship


def test_horizontal_ship_locator():
    battlefield = Battlefield(5, 5)
    horizontal_locator = HorizontalShipLocator(battlefield)

    ship = Ship(2)
    first_ship_located = horizontal_locator.locate_ship(ship, 2, 2)
    assert first_ship_located
    ship = Ship(1)
    second_ship_located = horizontal_locator.locate_ship(ship, 3, 2)
    assert not second_ship_located


def test_vertical_ship_locator():
    battlefield = Battlefield(5, 5)
    vertical_locator = VerticalShipLocator(battlefield)

    ship = Ship(2)
    first_ship_located = vertical_locator.locate_ship(ship, 2, 2)
    assert first_ship_located

    ship = Ship(1)
    second_ship_located = vertical_locator.locate_ship(ship, 2, 3)
    assert not second_ship_located


def test_vertical_ship_locator_outside_battle_field():
    battlefield = Battlefield(4, 4)
    vertical_locator = VerticalShipLocator(battlefield)

    ship = Ship(3)
    first_ship_located = vertical_locator.locate_ship(ship, 2, 2)
    assert not first_ship_located


def test_horizontal_ship_locator_outside_battle_field():
    battlefield = Battlefield(4, 4)
    horizontal_locator = HorizontalShipLocator(battlefield)

    ship = Ship(3)
    first_ship_located = horizontal_locator.locate_ship(ship, 2, 2)
    assert not first_ship_located
