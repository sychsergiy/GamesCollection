from games_collection.games.battleship.settings import BattleshipSettings
from games_collection.games.battleship.battleship_field import BattleshipField
from games_collection.game import AbstractGame
from games_collection.match import PlayerVsPlayerMatch

# ---------
from games_collection.actions_handler import ActionRegister

from games_collection.games.battleship.players_battleship_fields import (
    PlayersBattleshipFields
)
from games_collection.games.battleship.actions.locate_ship import (
    LocateShipActionHandler
)
from games_collection.games.battleship.actions.finish_ships_locating import (
    FinishShipsLocatingActionHandler
)
from games_collection.games.battleship.actions.shot import (
    ShotActionHandler
)


class BattleshipGame(AbstractGame):
    def __init__(
            self,
            match: PlayerVsPlayerMatch,
            settings: BattleshipSettings,
            players_battleship_fields: PlayersBattleshipFields
    ):
        self._players_battleship_fields = players_battleship_fields
        super(BattleshipGame, self).__init__(match, settings)

    def _register_actions_handlers(self):
        locate_ship_action_handler = LocateShipActionHandler(
            self._players_battleship_fields
        )
        finish_ships_locating_handler = FinishShipsLocatingActionHandler(
            self._players_battleship_fields
        )
        shot_action_handler = ShotActionHandler(
            self._players_battleship_fields, self._match,
        )

        locate_ship_action_register = ActionRegister(
            locate_ship_action_handler.action_class, locate_ship_action_handler
        )
        finish_ships_locating_action_register = ActionRegister(
            finish_ships_locating_handler.action_class,
            finish_ships_locating_handler
        )
        shot_action_register = ActionRegister(
            shot_action_handler.action_class,
            shot_action_handler
        )

        self._actions_handler.register(locate_ship_action_register)
        self._actions_handler.register(finish_ships_locating_action_register)
        self._actions_handler.register(shot_action_register)
