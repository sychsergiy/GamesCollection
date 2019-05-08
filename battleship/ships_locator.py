from enum import Enum

from battleship.battlefield import Battlefield
from battleship.ship import Ship


class RotationEnum(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class ShipsLocator(object):
    def __init__(self, battlefield: Battlefield):
        self._battlefield = battlefield

    def locate_ship(self, ship: Ship, x: int, y: int, rotation: RotationEnum):
        pass

