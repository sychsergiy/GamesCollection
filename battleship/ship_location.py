import typing as t

from enum import Enum

from battleship.cell import Cell
from battleship.ship import Ship


class ShipRotationEnum(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class ShipLocation(object):
    def __init__(
            self,
            ship: Ship,
            location: Cell,
            rotation: ShipRotationEnum,
    ):
        self.ship = ship
        self.location = location
        self.rotation = rotation

    def get_ship_cells(self) -> t.List[Cell]:
        if self.rotation == ShipRotationEnum.HORIZONTAL:
            locations = self._get_ship_horizontal_locations()
            return locations
        elif self.rotation == ShipRotationEnum.VERTICAL:
            locations = self._get_ship_vertical_locations()
            return locations

    def _get_ship_vertical_locations(self) -> t.List[Cell]:
        ship_locations = [
            Cell(self.location.x, self.location.y + i)
            for i in range(0, self.ship.size)
        ]
        return ship_locations

    def _get_ship_horizontal_locations(self) -> t.List[Cell]:
        ship_locations = [
            Cell(self.location.x + i, self.location.y)
            for i in range(0, self.ship.size)
        ]
        return ship_locations

    def get_last_location(self) -> Cell:
        if self.rotation == ShipRotationEnum.HORIZONTAL:
            last_cell = Cell(
                self.location.x + self.ship.size - 1, self.location.y
            )
            return last_cell
        elif self.rotation == ShipRotationEnum.VERTICAL:
            last_cell = Cell(
                self.location.x, self.location.y + self.ship.size - 1
            )
            return last_cell

    def get_busy_cells(self) -> t.List[Cell]:
        first_cell = self.location
        last_cell = self.get_last_location()

        top_left_corner_around = Cell(first_cell.x - 1, first_cell.y - 1)
        down_right_corner_around = Cell(last_cell.x + 1, last_cell.y + 1)

        locations = [
            Cell(x, y)
            for x in
            range(top_left_corner_around.x, down_right_corner_around.x + 1)
            for y in
            range(top_left_corner_around.y, down_right_corner_around.y + 1)
        ]
        return locations

    def get_cells_around(self) -> t.Set[Cell]:
        all_busy_locations = self.get_busy_cells()
        ship_locations = self.get_ship_cells()
        return set(all_busy_locations) - set(ship_locations)

    def is_ship_on_cell(self, location: Cell):
        return location in self.get_ship_cells()
