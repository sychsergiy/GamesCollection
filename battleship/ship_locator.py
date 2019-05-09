from battleship.battlefield import Battlefield
from battleship.ship_location import ShipLocation
from battleship.ships_location_storage import ShipsLocationStorage


class ShipLocator(object):
    def __init__(
            self,
            battlefield: Battlefield,
            ship_location_storage: ShipsLocationStorage
    ):
        self._battlefield = battlefield
        self._ship_location_storage = ship_location_storage

    def locate_ship(
            self, ship_location: ShipLocation
    ) -> bool:
        if self.is_ship_location_possible(ship_location):
            self._ship_location_storage.add_ship_location(ship_location)
            # todo: save to location to storage
            return True
        return False

    def is_ship_location_possible(self, ship_location: ShipLocation) -> bool:
        if not self.is_ship_location_inside_battlefield(ship_location):
            return False
        return not self.is_ships_nearby_present(ship_location)

    def is_ship_location_inside_battlefield(
            self, ship_location: ShipLocation
    ) -> bool:
        if not self._battlefield.is_location_inside(ship_location.location):
            return False
        last_ship_cell_location = ship_location.get_last_location()
        return self._battlefield.is_location_inside(last_ship_cell_location)

    def is_ships_nearby_present(
            self, ship_location: ShipLocation
    ) -> bool:
        busy_cells = self._ship_location_storage.get_busy_cells()
        ship_cells = ship_location.get_ship_cells()
        cells_intersection = busy_cells.intersection(ship_cells)
        return bool(cells_intersection)
