import typing as t

from battleship.battlefield_view import BattlefieldView
from battleship.game_mode import GameMode
from battleship.gun import Gun
from battleship.ships_locator import ShipsLocator
from battleship.ship_locator import ShipLocator
from battleship.ship_location import (
    VerticalShipLocation,
    HorizontalShipLocation,
)
from battleship.ship import Ship
from battleship.cell import Cell

from enum import Enum


class ShipRotationEnum(Enum):
    VERTICAL = 0
    HORIZONTAL = 1


class PlayerBattlefield(object):
    def __init__(
            self,
            game_mode: GameMode,

    ):
        # todo: located all ships from game_mode and than start game

        # todo: move all class to arguments
        self._ships_locator = ShipsLocator(game_mode.battlefield)
        self._gun = Gun(
            game_mode.battlefield, self._ships_locator
        )
        self._ship_locator = ShipLocator(
            game_mode.battlefield, self._ships_locator
        )
        self._view = BattlefieldView(
            game_mode.battlefield, self._ships_locator, self._gun
        )

    def locate_ship(
            self,
            x: int,
            y: int,
            ship_size: int,
            rotation: ShipRotationEnum = ShipRotationEnum.HORIZONTAL
    ) -> bool:
        assert isinstance(rotation, ShipRotationEnum)
        cell = Cell(x, y)
        ship = Ship(ship_size)
        if rotation == ShipRotationEnum.VERTICAL:
            ship_location = VerticalShipLocation(ship, cell)
        elif rotation == ShipRotationEnum.HORIZONTAL:
            ship_location = HorizontalShipLocation(ship, cell)
        return self._ship_locator.locate_ship(ship_location)

    @property
    def ships(self) -> t.List[Ship]:
        ships = [
            ship_location.ship for ship_location in
            self._ships_locator.ships_locations
        ]
        return ships

    def shot(self, x: int, y: int) -> Gun.ShotResultEnum:
        cell = Cell(x, y)
        # todo: try Except
        return self._gun.shot(cell)

    def is_game_over(self) -> bool:
        return all([ship.is_destroyed() for ship in self.ships])

    def print_battlefield_view(self, show_unwounded_ships_cells):
        # todo: remove method from current class
        self._view.draw(show_unwounded_ships_cells)
        for row in self._view.battlefield_matrix:
            print(row)
