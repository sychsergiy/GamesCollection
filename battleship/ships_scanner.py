import typing as t

from battleship.battlefield import Battlefield
from battleship.location import Location


class ShipsScanner(object):
    # todo: make horizontal, vertical and universal scanners
    def __init__(self, battlefield: Battlefield):
        self._battlefield = battlefield

    def _scan_cell(self, location: Location) -> t.Union[Location, None]:
        if not self._battlefield.is_location_inside(location):
            return None
        if self._battlefield.is_cell_with_ship(location):
            return location

    def _scan_top_cell(self, location: Location) -> t.Union[Location, None]:
        top_cell_location = Location(location.x, location.y + 1)
        return self._scan_cell(top_cell_location)

    def _scan_down_cell(self, location: Location) -> t.Union[Location, None]:
        down_cell_location = Location(location.x, location.y - 1)
        return self._scan_cell(down_cell_location)

    def _scan_left_cell(self, location: Location) -> t.Union[Location, None]:
        left_cell_location = Location(location.x - 1, location.y)
        return self._scan_cell(left_cell_location)

    def _scan_right_cell(self, location: Location) -> t.Union[Location, None]:
        right_cell_location = Location(location.x + 1, location.y)
        return self._scan_cell(right_cell_location)

    def _scan_left_top_corner(
            self, location: Location
    ) -> t.Union[Location, None]:
        left_top_corner_location = Location(location.x - 1, location.y + 1)
        return self._scan_cell(left_top_corner_location)

    def _scan_right_top_corner(
            self, location: Location
    ) -> t.Union[Location, None]:
        right_top_corner_location = Location(location.x + 1, location.y + 1)
        return self._scan_cell(right_top_corner_location)

    def _scan_left_down_corner(
            self, location: Location
    ) -> t.Union[Location, None]:
        left_down_corner_location = Location(location.x - 1, location.y - 1)
        return self._scan_cell(left_down_corner_location)

    def _scan_right_down_corner(
            self, location: Location
    ) -> t.Union[Location, None]:
        right_down_corner_location = Location(location.x + 1, location.y - 1)
        return self._scan_cell(right_down_corner_location)

    def scan_cell_with_location(self, location: Location) -> bool:
        # todo: return list of locations with found ships
        scanned_cells = [
            location for location in (
                self._scan_cell(location),
                self._scan_top_cell(location),
                self._scan_down_cell(location),
                self._scan_right_cell(location),
                self._scan_left_cell(location),
                self._scan_left_down_corner(location),
                self._scan_left_top_corner(location),
                self._scan_right_down_corner(location),
                self._scan_right_top_corner(location)
            )
        ]
        is_ships_found = any(scanned_cells)
        return is_ships_found
