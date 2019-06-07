from games_collection.games.battleship.actions.finish_ships_locating import (
    FinishShipsLocatingAction,
)
from games_collection.games.battleship.actions.locate_ship import (
    LocateShipAction,
)
from games_collection.games.battleship.actions.shot import ShotAction
from games_collection.games.battleship.battleship_field import BattleshipField
from games_collection.games.battleship.cell import Cell
from games_collection.games.battleship.game import BattleshipGame
from games_collection.games.battleship.players_battleship_fields import (
    PlayersBattleshipFields,
)
from games_collection.games.battleship.settings import short_match_settings
from games_collection.match import PlayerVsPlayerMatch
from games_collection.player import Player


def print_battlefield(battlefield_matrix):
    for row in battlefield_matrix:
        print("".join(row))


def run_battleship_demo():
    player1 = Player("Player1", 1)
    player2 = Player("Player2", 2)
    match = PlayerVsPlayerMatch(player1, player2)

    players_battleship_fields = PlayersBattleshipFields()
    players_battleship_fields.add_player_battleship_field(
        match.first_player, BattleshipField(short_match_settings)
    )
    players_battleship_fields.add_player_battleship_field(
        match.second_player, BattleshipField(short_match_settings)
    )

    battleship_game = BattleshipGame(
        match, short_match_settings, players_battleship_fields
    )

    battleship_game.send_action(LocateShipAction(player1, Cell(0, 0), 2))
    battleship_game.send_action(LocateShipAction(player1, Cell(2, 2), 2))
    result = battleship_game.send_action(
        LocateShipAction(player1, Cell(6, 6), 2)
    )

    print_battlefield(result.current_field)
    print()

    result = battleship_game.send_action(FinishShipsLocatingAction(player1))
    print(result.finished)

    battleship_game.send_action(LocateShipAction(player2, Cell(0, 0), 2))
    battleship_game.send_action(LocateShipAction(player2, Cell(4, 4), 2))
    result = battleship_game.send_action(
        LocateShipAction(player2, Cell(6, 6), 2)
    )

    print_battlefield(result.current_field)
    print()

    result = battleship_game.send_action(FinishShipsLocatingAction(player2))
    print(result.finished)

    for i in range(0, 8):
        for j in range(0, 8):
            result = battleship_game.send_action(
                ShotAction(player1, Cell(i, j))
            )
            if result.is_game_over:
                print_battlefield(result.player_field)
                print()
                print_battlefield(result.opponent_field)
                print(f"Game Over, player: {player1} winn")
                break

            print(f"First player shot result: {result.shot_result}")
            result = battleship_game.send_action(
                ShotAction(player2, Cell(i, j))
            )
            print(f"Second player shot result: {result.shot_result}")


if __name__ == "__main__":
    run_battleship_demo()
