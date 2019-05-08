from enum import Enum


class BattlefieldCell(object):
    class States(Enum):
        EMPTY = 1
        WITH_SHIP = 2
        EMPTY_HITED = 3
        WITH_HITED_SHIP = 4

    def __init__(self):
        self._state = self.States.EMPTY

    def __str__(self) -> str:
        return str(self._state.value)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value: States):
        assert isinstance(value, self.States)
        self._state = value


class Battlefield(object):
    def __init__(self, size: int):
        self.size = size
        self._cells_matrix = [
            [BattlefieldCell() for _ in range(size)]
            for _ in range(size)
        ]

    @property
    def cells(self) -> list:
        return self._cells_matrix

    def _get_cell(self, x: int, y: int) -> BattlefieldCell:
        return self._cells_matrix[x][y]

    def set_cell_state_empty(self, x: int, y: int):
        self._get_cell(x, y).state = BattlefieldCell.States.EMPTY

    def set_cell_state_empty_hited(self, x: int, y: int):
        self._get_cell(x, y).state = BattlefieldCell.States.EMPTY_HITED

    def set_cell_state_with_ship(self, x: int, y: int):
        self._get_cell(x, y).state = BattlefieldCell.States.WITH_SHIP

    def set_cell_state_with_hited_ship(self, x: int, y: int):
        self._get_cell(x, y).state = BattlefieldCell.States.WITH_HITED_SHIP

    def __str__(self) -> str:
        matrix_str = '\n'.join(
            [''.join([str(cell) for cell in cell_row])
             for cell_row in self._cells_matrix]
        )
        return matrix_str
