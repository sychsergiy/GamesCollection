from games_collection.games.battleship.cell import Cell
from games_collection.games.battleship.player.exceptions import (
    GameOverException
)
from games_collection.games.battleship.game.game import BattleshipGame
from games_collection.games.battleship.game_mode import short_game_mode
from games_collection.games.battleship.player.player import BattleshipPlayer

from games_collection.match import PlayerVsPlayerMatch
from games_collection.player import Player


def print_battlefield(battlefield_matrix):
    for row in battlefield_matrix:
        print(''.join(row))


user1 = Player("Player1", 1)
user2 = Player("Player2", 2)
match = PlayerVsPlayerMatch(user1, user2)
battleship_game = BattleshipGame(match, short_game_mode)

player1: BattleshipPlayer = battleship_game.create_game_player(user1)
player2: BattleshipPlayer = battleship_game.create_game_player(user2)

player1.locate_ship(Cell(0, 0), 2)
player1.locate_ship(Cell(2, 2), 2)
player1.locate_ship(Cell(6, 6), 2)

print_battlefield(player1.get_battlefield_view())
print()
print_battlefield(player1.get_opponent_battlefield_view())

locating_finished_1 = player1.finish_ships_locating_step()
print(locating_finished_1)

player2.locate_ship(Cell(0, 0), 2)
player2.locate_ship(Cell(4, 4), 2)
player2.locate_ship(Cell(6, 6), 2)

locating_finished_2 = player2.finish_ships_locating_step()
print(locating_finished_2)

for i in range(0, 8):
    for j in range(0, 8):
        try:
            shot_result_1 = player1.shot(Cell(i, j))
            print(f"First player shot result: {shot_result_1}")
            shot_result_2 = player2.shot(Cell(i, j))
            print(f"Second player shot result: {shot_result_2}")
        except GameOverException:
            # print(battleship_game.get_result_info())
            print_battlefield(player1.get_battlefield_view())
            print()
            print_battlefield(player2.get_battlefield_view())
            break
