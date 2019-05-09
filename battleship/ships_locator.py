from enum import Enum

from battleship.battlefield import Battlefield
from battleship.location import Location
from battleship.ship import Ship
from battleship.ships_scanner import ShipsScanner


class ShipRotationEnum(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class ShipLocator(object):
    def __init__(self, battlefield: Battlefield):
        self._battlefield = battlefield

    def locate_ship(self, ship: Ship, location: Location) -> bool:
        raise NotImplementedError

    def is_ship_location_possible(self, ship: Ship, location: Location) -> bool:
        ship_inside_battlefield = self.is_ship_location_inside_battlefield(
            ship, location
        )
        if not ship_inside_battlefield:
            return False

        nearby_ships_exits = self.is_ships_present_around_location(
            ship, location
        )
        return not nearby_ships_exits

    def is_ship_location_inside_battlefield(
            self, ship: Ship, location: Location
    ) -> bool:
        raise NotImplementedError

    def is_ships_present_around_location(
            self, ship: Ship, location: Location
    ) -> bool:
        raise NotImplementedError


class HorizontalShipLocator(ShipLocator):
    def locate_ship(self, ship: Ship, location: Location) -> bool:
        """
        :param ship: Ship instance
        :param location: координати x,у верхнього лівого кута
        """
        if not self.is_ship_location_possible(ship, location):
            return False
        for i in range(0, ship.size):
            ship_cell_location = Location(location.x + i, location.y)
            self._battlefield.set_cell_state_with_ship(ship_cell_location)
        return True

    def is_ships_present_around_location(
            self, ship: Ship, location: Location
    ) -> bool:
        ships_scanner = ShipsScanner(self._battlefield)
        for i in range(0, ship.size):
            cell_location = Location(location.x + i, location.y)
            ships_found = ships_scanner.scan_cell_with_location(cell_location)
            if ships_found:
                return True
        return False

    def is_ship_location_inside_battlefield(
            self, ship: Ship, location: Location
    ) -> bool:
        ship_last_cell_location = Location(
            location.x + ship.size - 1, location.y
        )
        return self._battlefield.is_location_inside(ship_last_cell_location)


class VerticalShipLocator(ShipLocator):
    def locate_ship(self, ship: Ship, location: Location) -> bool:
        if not self.is_ship_location_possible(ship, location):
            return False
        for i in range(0, ship.size):
            next_cell_location = Location(location.x, location.y + i)
            self._battlefield.set_cell_state_with_ship(next_cell_location)
        return True

    def is_ship_location_inside_battlefield(
            self, ship: Ship, location: Location
    ) -> bool:
        last_ship_cell_location = Location(
            location.x, location.y + ship.size - 1
        )
        return self._battlefield.is_location_inside(last_ship_cell_location)

    def is_ships_present_around_location(
            self, ship: Ship, location: Location
    ) -> bool:
        ships_scanner = ShipsScanner(self._battlefield)
        for i in range(0, ship.size):
            cell_location = Location(location.x, location.y + i)
            ships_found = ships_scanner.scan_cell_with_location(cell_location)
            if ships_found:
                return True
        return False
