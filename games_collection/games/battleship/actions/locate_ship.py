from games_collection.actions_handler import (
    AbstractAction,
    AbstractActionHandler,
    AbstractActionResult,
)
from games_collection.games.battleship.cell import Cell
from games_collection.games.battleship.players_battleship_fields import (
    PlayersBattleshipFields,
)
from games_collection.player import Player


class LocateShipAction(AbstractAction):
    def __init__(self, player: Player, cell: Cell, ship_size: int):
        self.player = player
        self.cell = cell
        self.ship_size = ship_size


class LocateShipActionResult(AbstractActionResult):
    def __init__(self, located: bool, ships_left: dict, current_field: list):
        self.located = located
        self.ships_left = ships_left
        self.current_field = current_field


class LocateShipActionHandler(AbstractActionHandler):
    action_class = LocateShipAction

    def __init__(self, players_battleship_fields: PlayersBattleshipFields):
        self._players_battleship_fields = players_battleship_fields

    def handle(self, action: LocateShipAction) -> LocateShipActionResult:
        super(LocateShipActionHandler, self).handle(action)
        battleship_field = self._players_battleship_fields.get_player_battleship_field(
            action.player
        )
        located = battleship_field.locate_ship(action.cell, action.ship_size)
        # todo: get ships_left from battleship_field.ships_counter
        action_result = LocateShipActionResult(
            located=located,
            ships_left={},
            current_field=battleship_field.get_battlefield_view(True),
        )
        return action_result
