from battleship.battlefield import Battlefield
from battleship.ship_location import ShipRotationEnum, ShipLocation
from battleship.ship_locator import ShipLocator
from battleship.ships_location_storage import ShipsLocationStorage
from battleship.ship import Ship
from battleship.cell import Cell


def test_horizontal_ship_locator():
    battlefield = Battlefield(5, 5)
    ships_location_storage = ShipsLocationStorage(battlefield)
    locator = ShipLocator(battlefield, ships_location_storage)
    ship = Ship(2)
    ship_location = ShipLocation(
        ship, Cell(2, 2), ShipRotationEnum.HORIZONTAL
    )

    first_ship_located = locator.locate_ship(ship_location)
    assert first_ship_located
    ship = Ship(1)
    ship_location = ShipLocation(
        ship, Cell(3, 2), ShipRotationEnum.HORIZONTAL
    )
    second_ship_located = locator.locate_ship(ship_location)
    assert not second_ship_located


def test_vertical_ship_locator():
    battlefield = Battlefield(5, 5)
    ships_location_storage = ShipsLocationStorage(battlefield)
    locator = ShipLocator(battlefield, ships_location_storage)

    ship = Ship(2)
    ship_location = ShipLocation(
        ship, Cell(2, 2), ShipRotationEnum.VERTICAL
    )
    first_ship_located = locator.locate_ship(ship_location)
    assert first_ship_located

    ship = Ship(1)
    ship_location = ShipLocation(
        ship, Cell(2, 3), ShipRotationEnum.VERTICAL
    )
    second_ship_located = locator.locate_ship(ship_location)
    assert not second_ship_located


def test_vertical_ship_locator_outside_battle_field():
    battlefield = Battlefield(4, 4)
    ships_location_storage = ShipsLocationStorage(battlefield)
    locator = ShipLocator(battlefield, ships_location_storage)

    ship = Ship(3)
    ship_location = ShipLocation(
        ship, Cell(2, 2), ShipRotationEnum.VERTICAL
    )
    first_ship_located = locator.locate_ship(ship_location)
    assert not first_ship_located


def test_horizontal_ship_locator_outside_battle_field():
    battlefield = Battlefield(4, 4)
    ships_location_storage = ShipsLocationStorage(battlefield)
    locator = ShipLocator(battlefield, ships_location_storage)

    ship = Ship(3)
    ship_location = ShipLocation(
        ship, Cell(2, 2), ShipRotationEnum.HORIZONTAL
    )
    first_ship_located = locator.locate_ship(ship_location)
    assert not first_ship_located
