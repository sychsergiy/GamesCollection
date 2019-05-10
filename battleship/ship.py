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
    def __init__(self, size: int):
        self._cells = [ShipCell() for _ in range(size)]

    @property
    def size(self):
        return len(self._cells)

    @property
    def health(self):
        return len([cell for cell in self._cells if not cell.destroyed])

    def is_destroyed(self) -> bool:
        return all([cell.destroyed for cell in self._cells])

    def is_alive(self) -> bool:
        return any([not cell.destroyed for cell in self._cells])

    def get_destroyed_cells_indexes(self):
        destroyed_cells_indexes = [
            self._cells.index(cell) for cell in self._cells if cell.destroyed
        ]
        return destroyed_cells_indexes

    def hit(self, cell_index: int) -> bool:
        cell_destroyed = self._cells[cell_index].hit()
        return cell_destroyed
