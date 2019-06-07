from games_collection.games.guess_number.guesses_counter import GuessesCounter
from games_collection.player import Player


class PlayersCounters(object):
    def __init__(self):
        self._players_counters_map = {}

    def add_player_counter(self, player: Player, counter: GuessesCounter):
        self._players_counters_map[player.id] = counter

    def get_player_counter(self, player: Player) -> GuessesCounter:
        if player.id not in self._players_counters_map:
            raise Exception("Player not in counters map")
        return self._players_counters_map[player.id]
