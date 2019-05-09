from enum import Enum

from battleship.location import Location


class BattlefieldCell(object):
    class States(Enum):
        EMPTY = 1
        WITH_SHIP = 2

    def __init__(self):
        self._state = self.States.EMPTY

    def __str__(self) -> str:
        return str(self._state.value)

    @property
    def state(self):
        return self._state

    def set_state_empty(self):
        self._state = self.States.EMPTY

    def set_state_with_ship(self):
        self._state = self.States.WITH_SHIP

    def is_empty(self) -> bool:
        return self._state == self.States.EMPTY

    def is_with_ship(self) -> bool:
        return self._state == self.States.WITH_SHIP


class Battlefield(object):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self._cells_matrix = None
        self._init_cells_matrix(width, height)

    def _init_cells_matrix(self, width: int, height: int):
        self._cells_matrix = [
            [BattlefieldCell() for _ in range(width)]
            for _ in range(height)
        ]

    @property
    def cells(self) -> list:
        return self._cells_matrix

    def _get_cell(self, location: Location) -> BattlefieldCell:
        x, y = location.y, location.x
        # swap x and y coordinates to go to standard coordinate system
        return self._cells_matrix[x][y]

    def set_cell_state_empty(self, location: Location):
        self._get_cell(location).set_state_empty()

    def set_cell_state_with_ship(self, location: Location):
        self._get_cell(location).set_state_with_ship()

    def is_location_inside(self, location: Location) -> bool:
        inside_x = 0 <= location.x < self.width
        inside_y = 0 <= location.y < self.height
        return inside_x and inside_y

    def is_cell_with_ship(self, location: Location) -> bool:
        cell = self._get_cell(location)
        return cell.is_with_ship()

    def is_cell_empty(self, location: Location) -> bool:
        cell = self._get_cell(location)
        return cell.is_empty()

    def __str__(self) -> str:
        matrix_str = '\n'.join(
            [''.join([str(cell) for cell in cell_row])
             for cell_row in self._cells_matrix]
        )
        return matrix_str
