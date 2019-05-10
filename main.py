from games_collection.games_collection import GamesCollection
from games_collection.games.battleship.game.game import BattleshipGame
from games_collection.games.battleship.game_mode import standard_game_mode

games_collection = GamesCollection([BattleshipGame(standard_game_mode)])
