from enum import Enum

from battleship.battlefield import Battlefield
from battleship.ship import Ship
from battleship.ships_scanner import ShipsScanner


class ShipRotationEnum(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class ShipLocator(object):
    def __init__(self, battlefield: Battlefield):
        self._battlefield = battlefield

    def locate_ship(self, ship: Ship, x: int, y: int) -> bool:
        raise NotImplementedError

    def is_ship_location_possible(self, ship, x, y) -> bool:
        ship_inside_battlefield = self.is_ship_location_inside_battlefield(
            ship, x, y
        )
        if not ship_inside_battlefield:
            return False

        nearby_ships_exits = self.is_ships_present_around_location(ship, x, y)
        return not nearby_ships_exits

    def is_ship_location_inside_battlefield(
            self, ship: Ship, x: int, y: int
    ) -> bool:
        raise NotImplementedError

    def is_ships_present_around_location(
            self, ship: Ship, x: int, y: int
    ) -> bool:
        raise NotImplementedError


class HorizontalShipLocator(ShipLocator):
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

    def is_ships_present_around_location(
            self, ship: Ship, x: int, y: int
    ) -> bool:
        ships_scanner = ShipsScanner(self._battlefield)
        for i in range(0, ship.size):
            ships_found = ships_scanner.scan_cell_with_location(x + i, y)
            if ships_found:
                return True
        return False

    def is_ship_location_inside_battlefield(
            self, ship: Ship, x: int, y: int
    ) -> bool:
        ship_last_cell_x = x + ship.size - 1
        return self._battlefield.is_location_inside(ship_last_cell_x, y)


class VerticalShipLocator(ShipLocator):
    def locate_ship(self, ship: Ship, x: int, y: int) -> bool:
        if not self.is_ship_location_possible(ship, x, y):
            return False
        for i in range(0, ship.size):
            self._battlefield.set_cell_state_with_ship(x, y + i)
        return True

    def is_ship_location_inside_battlefield(
            self, ship: Ship, x: int, y: int
    ) -> bool:
        last_ship_cell_y = y + ship.size - 1
        return self._battlefield.is_location_inside(x, last_ship_cell_y)

    def is_ships_present_around_location(
            self, ship: Ship, x: int, y: int
    ) -> bool:
        ships_scanner = ShipsScanner(self._battlefield)
        for i in range(0, ship.size):
            ships_found = ships_scanner.scan_cell_with_location(x, y + i)
            if ships_found:
                return True
        return False
