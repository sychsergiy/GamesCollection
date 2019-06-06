from games_collection.player import Player
from games_collection.games.guess_number.guesses_counter import GuessesCounter


class PlayersCounters(object):
    def __init__(self):
        self.players_counters_map = {}

    def add_player_counter(self, player: Player, counter: GuessesCounter):
        self.players_counters_map[player.id] = counter

    def get_player_counter(self, player: Player) -> GuessesCounter:
        # todo: handle player.id not in players_counter_map
        return self.players_counters_map[player.id]
