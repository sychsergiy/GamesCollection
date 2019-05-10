from games_collection.games_collection import GamesCollection
from games_collection.games.battleship.battleship_game import BattleshipGame

games_collection = GamesCollection([BattleshipGame])

print(games_collection.list_games())
print(games_collection.choose_game('Battleship'))
