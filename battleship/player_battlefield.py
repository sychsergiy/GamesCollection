import typing as t

from battleship.battlefield_view import BattlefieldView
from battleship.game_mode import GameMode
from battleship.player import Player
from battleship.ships_counter import ShipsCounter
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
            player: Player,
            game_mode: GameMode,

    ):
        # todo: move all class to arguments
        self._player = player
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
        self._ships_counter = ShipsCounter(game_mode)

        self._ships_locating_finished = False

    def locate_ship(
            self,
            cell: Cell,
            ship_size: int,
            rotation: ShipRotationEnum = ShipRotationEnum.HORIZONTAL
    ) -> bool:
        assert isinstance(rotation, ShipRotationEnum)

        ships_count = self._ships_counter.ships_with_size_left(ship_size)
        if ships_count == 0:
            return False

        ship = Ship(ship_size)
        if rotation == ShipRotationEnum.VERTICAL:
            ship_location = VerticalShipLocation(ship, cell)
        elif rotation == ShipRotationEnum.HORIZONTAL:
            ship_location = HorizontalShipLocation(ship, cell)

        ship_located = self._ship_locator.locate_ship(ship_location)
        if ship_located:
            self._ships_counter.retrieve_ship(ship_size)
        return ship_located

    # todo: add relocate ships method

    @property
    def ships(self) -> t.List[Ship]:
        ships = [
            ship_location.ship for ship_location in
            self._ships_locator.ships_locations
        ]
        return ships

    def shot(self, cell: Cell) -> Gun.ShotResultEnum:
        return self._gun.shot(cell)

    @property
    def all_ships_destroyed(self) -> bool:
        return all([ship.is_destroyed() for ship in self.ships])

    @property
    def ships_locating_finished(self) -> bool:
        return self._ships_locating_finished

    def finish_ships_locating(self) -> bool:
        if not self._ships_counter.is_all_ships_retrieved():
            return False
        else:
            self._ships_locating_finished = True
            return True

    def get_battlefield_view(self, show_unwounded_ships_cells):
        # todo: remove method from current class
        self._view.draw(show_unwounded_ships_cells)
        return self._view.battlefield_matrix
