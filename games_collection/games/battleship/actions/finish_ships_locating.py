from games_collection.actions_handler import (
    AbstractAction,
    AbstractActionResult,
    AbstractActionHandler,
)
from games_collection.games.battleship.players_battleship_fields import (
    PlayersBattleshipFields
)

from games_collection.player import Player


class FinishShipsLocatingAction(AbstractAction):
    def __init__(self, player: Player):
        self.player = player


class FinishShipsLocatingActionResult(AbstractActionResult):
    def __init__(self, finished: bool):
        self.finished = finished


class FinishShipsLocatingActionHandler(AbstractActionHandler):
    action_class = FinishShipsLocatingAction

    def __init__(self, players_battleship_fields: PlayersBattleshipFields):
        self._players_battleship_fields = players_battleship_fields

    def handle(
            self, action: FinishShipsLocatingAction
    ) -> FinishShipsLocatingActionResult:
        super(FinishShipsLocatingActionHandler, self).handle(action)

        battleship_field = (
            self._players_battleship_fields.get_player_battleship_field(
                action.player
            )
        )
        finished = battleship_field.finish_ships_locating()
        action_result = FinishShipsLocatingActionResult(finished)
        return action_result
