from battleship.battlefield import Battlefield
from battleship.ship_location import AbstractShipLocation
from battleship.ships_locator import ShipsLocator


class ShipLocator(object):
    def __init__(
            self,
            battlefield: Battlefield,
            ships_locator: ShipsLocator
    ):
        self._battlefield = battlefield
        self._ships_locator = ships_locator

    def locate_ship(
            self, ship_location: AbstractShipLocation
    ) -> bool:
        if self.is_ship_location_possible(ship_location):
            self._ships_locator.add_ship_location(ship_location)
            return True
        return False

    def is_ship_location_possible(
            self, ship_location: AbstractShipLocation
    ) -> bool:
        if not self.is_ship_location_inside_battlefield(ship_location):
            return False
        return not self.is_ships_nearby_present(ship_location)

    def is_ship_location_inside_battlefield(
            self, ship_location: AbstractShipLocation
    ) -> bool:
        if not self._battlefield.is_location_inside(
                ship_location.left_top_cell):
            return False
        last_ship_cell_location = ship_location.get_last_cell()
        return self._battlefield.is_location_inside(last_ship_cell_location)

    def is_ships_nearby_present(
            self, ship_location: AbstractShipLocation
    ) -> bool:
        busy_cells = self._ships_locator.get_busy_cells()
        ship_cells = ship_location.get_ship_cells()
        cells_intersection = busy_cells.intersection(ship_cells)
        return bool(cells_intersection)
