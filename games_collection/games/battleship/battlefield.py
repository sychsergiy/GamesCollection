import typing as t

from games_collection.games.battleship.cell import Cell


class Battlefield(object):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def is_cell_internal(self, cell: Cell) -> bool:
        inside_x = 0 <= cell.x < self.width
        inside_y = 0 <= cell.y < self.height
        return inside_x and inside_y

    @property
    def cells(self) -> t.Set[Cell]:
        cells = {
            Cell(x, y) for x in range(self.width) for y in range(self.height)
        }
        return cells
