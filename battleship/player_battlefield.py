from battleship.battlefield import Battlefield
from battleship.shot_manager import ShotManager
from battleship.ships_locator import ShipsLocator
from battleship.ship_locator import ShipLocator
from battleship.ship_location import (
    VerticalShipLocation,
)
from battleship.ship import Ship
from battleship.cell import Cell


class PlayerBattlefield(object):
    def __init__(self, battlefield: Battlefield):
        self._battlefield = battlefield
        self._ships_locator = ShipsLocator(battlefield)
        self._ship_locator = ShipLocator(battlefield, self._ships_locator)
        self._shot_manager = ShotManager(self._ships_locator)
        # todo: refactor
        self._ships = None
        self._locate_ships()

    def _locate_ships(self):
        ships_locations = [
            VerticalShipLocation(Ship(2), Cell(0, 0)),
            VerticalShipLocation(Ship(1), Cell(4, 4)),
            VerticalShipLocation(Ship(1), Cell(4, 0)),
            VerticalShipLocation(Ship(1), Cell(0, 4)),
        ]
        self._ships = [ship_location.ship for ship_location in ships_locations]
        for ship_location in ships_locations:
            self._ship_locator.locate_ship(ship_location)

    def shot(self, x: int, y: int):
        cell = Cell(x, y)
        return self._shot_manager.shot(cell)

    def is_game_over(self):
        return all([ship.is_destroyed() for ship in self._ships])

    def get_current_battlefield_state(self, show_unwounded_ships_cells=True):
        # todo: add separate class to draw battlefield
        battlefield_matrix = [
            # empty cells
            ['0' for _ in range(self._battlefield.width)]
            for _ in range(self._battlefield.height)
        ]

        for cell in self._shot_manager.hited_cells:
            # hited cells
            battlefield_matrix[cell.y][cell.x] = '1'

        for ship_location in self._ships_locator.ships_locations:
            if ship_location.ship.is_destroyed():
                for cell in ship_location.get_ship_cells():
                    # destroyed ship
                    battlefield_matrix[cell.y][cell.x] = '2'

            else:
                ship_cells = ship_location.get_ship_cells()
                if show_unwounded_ships_cells:
                    for cell in ship_cells:
                        # unwounded ship cells
                        battlefield_matrix[cell.y][cell.x] = '3'

                for index in ship_location.ship.get_destroyed_cells_indexes():
                    ship_cell = ship_cells[index]
                    # wounded but not destroyed ship cells
                    battlefield_matrix[ship_cell.y][ship_cell.x] = '4'
        return battlefield_matrix
