import typing as t
from enum import Enum

from battleship.battlefield import Battlefield
from battleship.location import Location
from battleship.ship import Ship


class ShipRotationEnum(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class ShipLocation(object):
    def __init__(
            self,
            ship: Ship,
            location: Location,
            rotation: ShipRotationEnum,
    ):
        self.ship = ship
        self.location = location
        self.rotation = rotation

    def get_ship_cells(self) -> t.List[Location]:
        if self.rotation == ShipRotationEnum.HORIZONTAL:
            locations = self._get_ship_horizontal_locations()
            return locations
        elif self.rotation == ShipRotationEnum.VERTICAL:
            locations = self._get_ship_vertical_locations()
            return locations

    def _get_ship_vertical_locations(self) -> t.List[Location]:
        ship_locations = [
            Location(self.location.x, self.location.y + i)
            for i in range(0, self.ship.size)
        ]
        return ship_locations

    def _get_ship_horizontal_locations(self) -> t.List[Location]:
        ship_locations = [
            Location(self.location.x + i, self.location.y)
            for i in range(0, self.ship.size)
        ]
        return ship_locations

    def get_last_location(self) -> Location:
        if self.rotation == ShipRotationEnum.HORIZONTAL:
            last_cell = Location(
                self.location.x + self.ship.size - 1, self.location.y
            )
            return last_cell
        elif self.rotation == ShipRotationEnum.VERTICAL:
            last_cell = Location(
                self.location.x, self.location.y + self.ship.size - 1
            )
            return last_cell

    def get_busy_cells(self) -> t.List[Location]:
        first_cell = self.location
        last_cell = self.get_last_location()

        top_left_corner_around = Location(first_cell.x - 1, first_cell.y - 1)
        down_right_corner_around = Location(last_cell.x + 1, last_cell.y + 1)

        locations = [
            Location(x, y)
            for x in
            range(top_left_corner_around.x, down_right_corner_around.x + 1)
            for y in
            range(top_left_corner_around.y, down_right_corner_around.y + 1)
        ]
        return locations

    def get_cells_around(self) -> t.Set[Location]:
        all_busy_locations = self.get_busy_cells()
        ship_locations = self.get_ship_cells()
        return set(all_busy_locations) - set(ship_locations)

    def is_ship_on_cell(self, location: Location):
        return location in self.get_ship_cells()


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

    def get_busy_cell_with_ships(self) -> t.Set[Location]:
        cells_with_ships = set()
        for ship_location in self._ship_locations:
            cells_with_ships = cells_with_ships.union(
                ship_location.get_ship_cells()
            )
        return cells_with_ships

    def get_busy_cells_with_ships_nearby(self) -> t.Set[Location]:
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

    def get_ship_by_cell(self, location: Location) -> t.Union[None, Ship]:
        for ship_location in self._ship_locations:
            if ship_location.is_ship_on_cell(location):
                return ship_location.ship


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
