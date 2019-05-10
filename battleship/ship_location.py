import typing as t

from enum import Enum

from battleship.cell import Cell
from battleship.ship import Ship


class ShipRotationEnum(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class AbstractShipLocation(object):
    def __init__(
            self,
            ship: Ship,
            cell: Cell,
    ):
        self.ship = ship
        self.left_top_cell = cell

    def get_ship_cells(self) -> t.List[Cell]:
        raise NotImplementedError

    def get_last_cell(self) -> Cell:
        raise NotImplementedError

    def get_busy_cells(self) -> t.List[Cell]:
        first_cell = self.left_top_cell
        last_cell = self.get_last_cell()

        top_left_corner_around = Cell(first_cell.x - 1, first_cell.y - 1)
        down_right_corner_around = Cell(last_cell.x + 1, last_cell.y + 1)

        cells = [
            Cell(x, y)
            for x in
            range(top_left_corner_around.x, down_right_corner_around.x + 1)
            for y in
            range(top_left_corner_around.y, down_right_corner_around.y + 1)
        ]
        return cells

    def get_cells_around(self) -> t.Set[Cell]:
        all_busy_cells = self.get_busy_cells()
        ship_cells = self.get_ship_cells()
        return set(all_busy_cells) - set(ship_cells)

    def is_ship_on_cell(self, cell: Cell):
        return cell in self.get_ship_cells()

    def get_ship_cell_index(self, cell: Cell) -> t.Union[int, None]:
        ship_cells = self.get_ship_cells()
        if cell in ship_cells:
            return ship_cells.index(cell)


class VerticalShipLocation(AbstractShipLocation):
    def get_last_cell(self) -> Cell:
        last_cell = Cell(
            self.left_top_cell.x, self.left_top_cell.y + self.ship.size - 1
        )
        return last_cell

    def get_ship_cells(self) -> t.List[Cell]:
        ship_cells = [
            Cell(self.left_top_cell.x, self.left_top_cell.y + i)
            for i in range(0, self.ship.size)
        ]
        return ship_cells


class HorizontalShipLocation(AbstractShipLocation):
    def get_last_cell(self):
        last_cell = Cell(
            self.left_top_cell.x + self.ship.size - 1, self.left_top_cell.y
        )
        return last_cell

    def get_ship_cells(self) -> t.List[Cell]:
        ship_cells = [
            Cell(self.left_top_cell.x + i, self.left_top_cell.y)
            for i in range(0, self.ship.size)
        ]
        return ship_cells
