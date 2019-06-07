from games_collection.actions_handler import (
    AbstractAction,
    AbstractActionResult,
    AbstractActionHandler,
)

from games_collection.games.battleship.cell import Cell


class LocateShipAction(AbstractAction):
    def __init__(self, cell: Cell, ship_size: int):
        self.cell = cell
        self.ship_size = ship_size


class LocateShipActionResult(AbstractActionResult):
    def __init__(self, located: bool, ships_left: dict):
        self.located = located
        self.ships_left = ships_left
