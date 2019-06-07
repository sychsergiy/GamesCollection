from games_collection.actions_handler import (
    AbstractAction,
    AbstractActionResult,
    AbstractActionHandler
)
from games_collection.games.battleship.battleship_field import BattleshipField
from games_collection.games.battleship.cell import Cell
from games_collection.games.battleship.gun import Gun
from games_collection.games.battleship.players_battleship_fields import (
    PlayersBattleshipFields
)
from games_collection.match import PlayerVsPlayerMatch
from games_collection.player import Player


class ShotAction(AbstractAction):
    def __init__(self, player: Player, cell: Cell):
        self.player = player
        self.cell = cell


class ShotActionResult(AbstractActionResult):
    def __init__(
            self,
            shot_result: Gun.ShotResultEnum,
            player_field: BattleshipField,
            opponent_field: BattleshipField,
            is_game_over: bool = False
    ):
        self.shot_result = shot_result
        self.player_field = player_field
        self.opponent_field = opponent_field
        self.is_game_over = is_game_over


class ShotActionHandler(AbstractActionHandler):
    action_class = ShotAction

    def __init__(
            self,
            players_battleship_fields: PlayersBattleshipFields,
            match: PlayerVsPlayerMatch,
    ):
        self._match = match
        self._players_battleship_fields = players_battleship_fields

    def handle(self, action: ShotAction) -> ShotActionResult:
        from games_collection.games.battleship.exceptions import (
            PlayerShipsNotLocatedException,
            OpponentShipsNotLocatedException,
            OpponentTurnException,

        )
        battleship_field = (
            self._players_battleship_fields.get_player_battleship_field(
                action.player
            )
        )
        if not battleship_field.ships_locating_finished:
            raise PlayerShipsNotLocatedException("Player ships not located")

        opponent_battleship_field = (
            self._players_battleship_fields.get_opponent_battleship_field(
                action.player
            )
        )
        if not opponent_battleship_field:
            raise OpponentShipsNotLocatedException("Opponent ships not located")
        if not self._match.is_player_turn(action.player):
            raise OpponentTurnException("It is opponent turn now")

        shot_result = opponent_battleship_field.shot(action.cell)
        is_game_over = False
        if shot_result == Gun.ShotResultEnum.SHIP_DESTROYED:
            is_game_over = opponent_battleship_field.all_ships_destroyed
        self._match.finish_current_player_turn()
        action_result = ShotActionResult(
            shot_result=shot_result,
            is_game_over=is_game_over,
            opponent_field=opponent_battleship_field.get_battlefield_view(
                False),
            player_field=opponent_battleship_field.get_battlefield_view(False),
        )
        return action_result
