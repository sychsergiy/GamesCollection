import typing as t

from battleship.battlefield import Battlefield
from battleship.ship_location import AbstractShipLocation
from battleship.ship import Ship
from battleship.cell import Cell


class ShipsLocator(object):
    def __init__(self, battlefield: Battlefield):
        self._battlefield = battlefield
        self._ships_locations: t.Set[AbstractShipLocation] = set()

    def get_busy_cells(self):
        cells_with_ships = set()
        for ship_location in self._ships_locations:
            cells_with_ships = cells_with_ships.union(
                ship_location.get_busy_cells()
            )
        return cells_with_ships

    def get_busy_cells_with_ships(self) -> t.Set[Cell]:
        cells_with_ships = set()
        for ship_location in self._ships_locations:
            cells_with_ships = cells_with_ships.union(
                ship_location.get_ship_cells()
            )
        return cells_with_ships

    def get_busy_cells_with_ships_nearby(self) -> t.Set[Cell]:
        cells_around_ships = set()
        for ship_location in self._ships_locations:
            cells_around_ships = cells_around_ships.union(
                ship_location.get_cells_around()
            )
        cells_around_ships_inside_battlefield = {
            cell for cell in cells_around_ships
            if self._battlefield.is_cell_internal(cell)
        }
        return cells_around_ships_inside_battlefield

    def _add_ship_location(self, ship_location: AbstractShipLocation):
        self._ships_locations.add(ship_location)

    def get_ship_by_cell(self, cell: Cell) -> t.Union[None, Ship]:
        return self.get_ship_location_by_cell(cell).ship

    def get_ship_location_by_cell(
            self, cell: Cell
    ) -> t.Union[None, AbstractShipLocation]:
        for ship_location in self._ships_locations:
            if ship_location.is_ship_on_cell(cell):
                return ship_location

    @property
    def ships_locations(self):
        return self._ships_locations
