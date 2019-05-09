import typing as t

from battleship.battlefield import Battlefield
from battleship.ship_location import ShipLocation
from battleship.ship import Ship
from battleship.cell import Cell


class ShipsLocationStorage(object):
    def __init__(self, battlefield: Battlefield):
        self._battlefield = battlefield
        self._ship_locations: t.Set[ShipLocation] = set()

    def get_busy_cells(self):
        cells_with_ships = set()
        for ship_location in self._ship_locations:
            cells_with_ships = cells_with_ships.union(
                ship_location.get_busy_cells()
            )
        return cells_with_ships

    def get_busy_cell_with_ships(self) -> t.Set[Cell]:
        cells_with_ships = set()
        for ship_location in self._ship_locations:
            cells_with_ships = cells_with_ships.union(
                ship_location.get_ship_cells()
            )
        return cells_with_ships

    def get_busy_cells_with_ships_nearby(self) -> t.Set[Cell]:
        cells_around_ships = set()
        for ship_location in self._ship_locations:
            cells_around_ships = cells_around_ships.union(
                ship_location.get_cells_around()
            )
        cells_around_ships_inside_battlefield = {
            cell for cell in cells_around_ships
            if self._battlefield.is_location_inside(cell)
        }
        return cells_around_ships_inside_battlefield

    def add_ship_location(self, ship_location: ShipLocation):
        self._ship_locations.add(ship_location)

    def get_ship_by_cell(self, location: Cell) -> t.Union[None, Ship]:
        for ship_location in self._ship_locations:
            if ship_location.is_ship_on_cell(location):
                return ship_location.ship
