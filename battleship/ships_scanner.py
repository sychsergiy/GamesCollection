from battleship.battlefield import Battlefield


class ShipsScanner(object):
    # todo: make horizontal, vertical and universal scanners
    def __init__(self, battlefield: Battlefield):
        self._battlefield = battlefield

    def _scan_cell(self, x: int, y: int):
        if not self._battlefield.is_location_inside(x, y):
            return None
        if self._battlefield.is_cell_with_ship(x, y):
            return x, y

    def _scan_top_cell(self, x: int, y: int):
        return self._scan_cell(x, y + 1)

    def _scan_down_cell(self, x: int, y: int):
        return self._scan_cell(x, y - 1)

    def _scan_left_cell(self, x: int, y: int):
        return self._scan_cell(x - 1, y)

    def _scan_right_cell(self, x: int, y: int):
        return self._scan_cell(x + 1, y)

    def _scan_left_top_corner(self, x: int, y: int):
        return self._scan_cell(x - 1, y + 1)

    def _scan_right_top_corner(self, x: int, y: int):
        return self._scan_cell(x + 1, y + 1)

    def _scan_left_down_corner(self, x: int, y: int):
        return self._scan_cell(x - 1, y - 1)

    def _scan_right_down_corner(self, x: int, y: int):
        return self._scan_cell(x + 1, y - 1)

    def scan_cell_with_location(self, x: int, y: int) -> bool:
        # todo: return list of locations with found ships
        scanned_cells = [
            location for location in (
                self._scan_cell(x, y),
                self._scan_top_cell(x, y),
                self._scan_down_cell(x, y),
                self._scan_right_cell(x, y),
                self._scan_left_cell(x, y),
                self._scan_left_down_corner(x, y),
                self._scan_left_top_corner(x, y),
                self._scan_right_down_corner(x, y),
                self._scan_right_top_corner(x, y)
            )
        ]
        is_ships_found = any(scanned_cells)
        return is_ships_found
