from enum import Enum

from battleship.battlefield import Battlefield
from battleship.ship import Ship


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
        # todo: check if there are no ships already located on this cells or nearby
        for i in range(0, ship.size):
            self._battlefield.set_cell_state_with_ship(x + i, y)
        return True

    def is_ship_location_possible(self, ship, x, y) -> bool:
        raise NotImplementedError


class VerticalShipsLocator(ShipsLocator):
    def locate_ship(self, ship: Ship, x: int, y: int) -> bool:
        # todo: check if there are no ships already located on this cells or nearby
        for i in range(0, ship.size):
            self._battlefield.set_cell_state_with_ship(x, y + i)
        return True

    def is_ship_location_possible(self, ship, x, y) -> bool:
        raise NotImplementedError
