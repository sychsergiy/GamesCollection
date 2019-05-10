from battleship.battlefield import Battlefield
from battleship.ships_locator import ShipsLocator
from battleship.gun import Gun
from battleship.cell import Cell


class BattlefieldView(object):
    def __init__(
            self,
            battlefield: Battlefield,
            ships_locator: ShipsLocator,
            shot_manager: Gun
    ):
        self._ships_locator = ships_locator
        self._shot_manager = shot_manager

        self._battlefield_matrix = None
        self._draw_empty_cells(battlefield)

    def _draw_empty_cells(self, battlefield: Battlefield):
        self._battlefield_matrix = [
            # empty cells
            [' 0 ' for _ in range(battlefield.width)]
            for _ in range(battlefield.height)
        ]

    def _get_matrix_cell(self, cell: Cell):
        # swap (x,y) coordinates to go to the standard coordinate system
        return self._battlefield_matrix[cell.y][cell.x]

    def _set_matrix_cell(self, cell: Cell, value):
        # swap (x,y) coordinates to go to the standard coordinate system
        self._battlefield_matrix[cell.y][cell.x] = value

    def _draw_hited_cells(self):
        for cell in self._shot_manager.hited_cells:
            self._set_matrix_cell(cell, ' * ')

    def _draw_ships(self, show_unwounded_ships_cells: bool):
        for ship_location in self._ships_locator.ships_locations:
            if ship_location.ship.is_destroyed():
                for cell in ship_location.get_ship_cells():
                    # destroyed ships
                    self._set_matrix_cell(cell, '[x]')
            else:
                ship_cells = ship_location.get_ship_cells()
                if show_unwounded_ships_cells:
                    for cell in ship_cells:
                        # unwounded ship cells
                        self._set_matrix_cell(cell, '[ ]')

                for index in ship_location.ship.get_destroyed_cells_indexes():
                    ship_cell = ship_cells[index]
                    # wounded but not destroyed ship cells
                    self._set_matrix_cell(ship_cell, '[*]')

    def draw(self, show_unwounded_ships_cells: bool):
        # self._draw_empty_cells() // already called in __init__ todo: refactor
        self._draw_hited_cells()
        self._draw_ships(show_unwounded_ships_cells)

    @property
    def battlefield_matrix(self):
        return self._battlefield_matrix
