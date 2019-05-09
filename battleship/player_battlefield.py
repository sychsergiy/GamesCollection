import typing as t

from battleship.battlefield import Battlefield
from battleship.shot_manager import ShotManager, ShotResultEnum
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
    def __init__(self, battlefield_width: int, battlefield_height: int):
        self._battlefield = Battlefield(battlefield_width, battlefield_height)
        self._ships_locator = ShipsLocator(self._battlefield)
        self._shot_manager = ShotManager(self._ships_locator)
        self._ship_locator = ShipLocator(self._battlefield, self._ships_locator)

        self._view = BattlefieldView(
            self._battlefield, self._ships_locator, self._shot_manager
        )

        self._locate_ships()

    def _locate_ships(self):
        ships_locations = [
            VerticalShipLocation(Ship(2), Cell(0, 0)),
            VerticalShipLocation(Ship(1), Cell(4, 4)),
            VerticalShipLocation(Ship(1), Cell(4, 0)),
            VerticalShipLocation(Ship(1), Cell(0, 4)),
        ]
        self._ships = [ship_location.ship for ship_location in ships_locations]
        for ship_location in ships_locations:
            self._ship_locator.locate_ship(ship_location)

    def locate_ship(
            self,
            x: int,
            y: int,
            size: int,
            rotation: ShipRotationEnum = ShipRotationEnum.HORIZONTAL
    ) -> bool:
        assert isinstance(rotation, ShipRotationEnum)
        cell = Cell(x, y)
        ship = Ship(size)
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

    def shot(self, x: int, y: int) -> ShotResultEnum:
        cell = Cell(x, y)
        if not self._battlefield.is_cell_internal(cell):
            raise Exception('cell outside battlefield')
        return self._shot_manager.shot(cell)

    def is_game_over(self) -> bool:
        return all([ship.is_destroyed() for ship in self.ships])

    def print_battlefield_view(self, show_unwounded_ships_cells):
        # todo: remove method from current class
        self._view.draw(show_unwounded_ships_cells)
        for row in self._view.battlefield_matrix:
            print(row)


class BattlefieldView(object):
    def __init__(
            self,
            battlefield: Battlefield,
            ships_locator: ShipsLocator,
            shot_manager: ShotManager
    ):
        self._ships_locator = ships_locator
        self._shot_manager = shot_manager

        self._battlefield_matrix = None
        self._draw_empty_cells(battlefield)

    def _draw_empty_cells(self, battlefield: Battlefield):
        self._battlefield_matrix = [
            # empty cells
            ['0' for _ in range(battlefield.width)]
            for _ in range(battlefield.height)
        ]

    def _get_matrix_cell(self, cell: Cell):
        # swap (x,y) coordinates to go to the standard coordinate system
        return self._battlefield_matrix[cell.y][cell.x]

    def _set_matrix_cell(self, cell: Cell, value):
        # swap (x,y) coordinates to go to the standard coordinate system
        self._battlefield_matrix[cell.y][cell.x] = value

    def _draw_hited_cells(self):
        for cell in self._shot_manager.hited_cells:
            self._set_matrix_cell(cell, '1')

    def _draw_ships(self, show_unwounded_ships_cells: bool):
        for ship_location in self._ships_locator.ships_locations:
            if ship_location.ship.is_destroyed():
                for cell in ship_location.get_ship_cells():
                    # destroyed ships
                    self._set_matrix_cell(cell, '2')
            else:
                ship_cells = ship_location.get_ship_cells()
                if show_unwounded_ships_cells:
                    for cell in ship_cells:
                        # unwounded ship cells
                        self._set_matrix_cell(cell, '3')

                for index in ship_location.ship.get_destroyed_cells_indexes():
                    ship_cell = ship_cells[index]
                    # wounded but not destroyed ship cells
                    self._set_matrix_cell(ship_cell, '4')

    def draw(self, show_unwounded_ships_cells: bool):
        # self._draw_empty_cells() // already called in __init__ todo: refactor
        self._draw_hited_cells()
        self._draw_ships(show_unwounded_ships_cells)

    @property
    def battlefield_matrix(self):
        return self._battlefield_matrix
