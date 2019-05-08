from enum import Enum

from battleship.battlefield import Battlefield
from battleship.ship import Ship
from battleship.ships_scanner import ShipsScanner


class ShipRotationEnum(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class ShipsLocator(object):
    def __init__(self, battlefield: Battlefield):
        self._battlefield = battlefield

    def locate_ship(self, ship: Ship, x: int, y: int) -> bool:
        raise NotImplementedError

    def is_ship_location_possible(self, ship, x, y) -> bool:
        raise NotImplementedError


class HorizontalShipsLocator(ShipsLocator):
    def locate_ship(self, ship: Ship, x: int, y: int) -> bool:
        """
        :param ship: Ship instance
        :param x: координата по x верхнього лівого кута
        :param y: координата по у верхнього лівого кута
        """
        if not self.is_ship_location_possible(ship, x, y):
            return False
        for i in range(0, ship.size):
            self._battlefield.set_cell_state_with_ship(x + i, y)
        return True

    def is_ship_location_possible(self, ship, x, y) -> bool:
        ships_scanner = ShipsScanner(self._battlefield)
        for i in range(0, self._battlefield.width):
            ships_found = ships_scanner.scan_cell_with_location(x + i, y)
            if ships_found:
                return False
        return True


class VerticalShipsLocator(ShipsLocator):
    def locate_ship(self, ship: Ship, x: int, y: int) -> bool:
        if not self.is_ship_location_possible(ship, x, y):
            return False
        for i in range(0, ship.size):
            self._battlefield.set_cell_state_with_ship(x, y + i)
        return True

    def is_ship_location_possible(self, ship, x, y) -> bool:
        ships_scanner = ShipsScanner(self._battlefield)
        for i in range(0, self._battlefield.height):
            ships_found = ships_scanner.scan_cell_with_location(x, y + i)
            if ships_found:
                return False
        return True
