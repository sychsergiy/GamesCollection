from enum import Enum


class ShipCell(object):
    def __init__(self):
        self._destroyed = False

    def hit(self) -> bool:
        if not self._destroyed:
            self._destroyed = True
            return True
        return False

    @property
    def destroyed(self):
        return self._destroyed


class Ship(object):
    class RotationEnum(Enum):
        HORIZONTAL = 1
        VERTICAL = 2

    def __init__(self, size: int):
        self._rotation = self.RotationEnum.HORIZONTAL
        self._cells = [ShipCell() for _ in range(size)]

    @property
    def size(self):
        return len(self._cells)

    def is_alive(self):
        return all([cell.destroyed for cell in self._cells])

    def is_wounded(self):
        return any([cell.destroyed for cell in self._cells])

    def hit_cell(self, cell_index: int) -> bool:
        return self._cells[cell_index].hit()
