from games_collection.player import Player


class PlayerVsPlayerMatch(object):
    def __init__(
        self, first_player: Player = None, second_player: Player = None
    ):
        self.first_player = first_player
        self.second_player = second_player

        self._current_turn_player_id = first_player.id

    def is_player_turn(self, player: Player):
        return self._current_turn_player_id == player.id

    def finish_current_player_turn(self):
        if self._current_turn_player_id == self.first_player.id:
            self._current_turn_player_id = self.second_player.id
        elif self._current_turn_player_id == self.second_player.id:
            self._current_turn_player_id = self.first_player.id
