from games_collection.games.battleship.battlefield import Battlefield
from games_collection.games.battleship.ship_location import (
    HorizontalShipLocation,
    VerticalShipLocation,
)
from games_collection.games.battleship.ship_locator import ShipLocator
from games_collection.games.battleship.ships_locator import ShipsLocator
from games_collection.games.battleship.ship import Ship
from games_collection.games.battleship.cell import Cell


def test_horizontal_ship_location():
    battlefield = Battlefield(5, 5)
    ships_location_storage = ShipsLocator(battlefield)
    locator = ShipLocator(battlefield, ships_location_storage)
    ship = Ship(2)
    ship_location = HorizontalShipLocation(ship, Cell(2, 2))

    first_ship_located = locator.locate_ship(ship_location)
    assert first_ship_located
    ship = Ship(1)
    ship_location = HorizontalShipLocation(ship, Cell(3, 2))
    second_ship_located = locator.locate_ship(ship_location)
    assert not second_ship_located


def test_vertical_ship_location():
    battlefield = Battlefield(5, 5)
    ships_location_storage = ShipsLocator(battlefield)
    locator = ShipLocator(battlefield, ships_location_storage)

    ship = Ship(2)
    ship_location = VerticalShipLocation(ship, Cell(2, 2))
    first_ship_located = locator.locate_ship(ship_location)
    assert first_ship_located

    ship = Ship(1)
    ship_location = VerticalShipLocation(ship, Cell(2, 3))
    second_ship_located = locator.locate_ship(ship_location)
    assert not second_ship_located


def test_vertical_ship_location_outside_battle_field():
    battlefield = Battlefield(4, 4)
    ships_location_storage = ShipsLocator(battlefield)
    locator = ShipLocator(battlefield, ships_location_storage)

    ship = Ship(3)
    ship_location = VerticalShipLocation(ship, Cell(2, 2))
    first_ship_located = locator.locate_ship(ship_location)
    assert not first_ship_located


def test_horizontal_ship_location_outside_battle_field():
    battlefield = Battlefield(4, 4)
    ships_location_storage = ShipsLocator(battlefield)
    locator = ShipLocator(battlefield, ships_location_storage)
    ship = Ship(3)
    ship_location = HorizontalShipLocation(ship, Cell(2, 2))
    first_ship_located = locator.locate_ship(ship_location)
    assert not first_ship_located
