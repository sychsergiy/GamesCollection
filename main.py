from games_collection.games.battleship.cell import Cell
from games_collection.games.battleship.player.exceptions import \
    GameOverException
from games_collection.games.battleship.player.player import BattleshipPlayer
from games_collection.games_collection import GamesCollection
from games_collection.games.battleship.game.game import BattleshipGame
from games_collection.games.battleship.game_mode import short_game_mode
from games_collection.player import Player


def print_battlefield(battlefield_matrix):
    for row in battlefield_matrix:
        print(''.join(row))


games_collection = GamesCollection([BattleshipGame(short_game_mode)])

battleship_game = games_collection.choose_game("Battleship")

player1 = BattleshipPlayer(Player("Player1", 1))
player2 = BattleshipPlayer(Player("Player2", 2))

battleship_game.connect_player(player1)
battleship_game.connect_player(player2)

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
            shot_result_2 = player2.shot(Cell(i, j))
            # print(f"First player shot result: {shot_result_1}")
            # print(f"Second player shot result: {shot_result_2}")
        except GameOverException:
            print(battleship_game.get_result_info())
            print_battlefield(player1.get_battlefield_view())
            print()
            print_battlefield(player1.get_opponent_battlefield_view())
            break
