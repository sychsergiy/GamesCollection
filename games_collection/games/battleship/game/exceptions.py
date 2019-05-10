class BattleshipGameException(Exception):
    pass


class PlayerNotConnectedException(BattleshipGameException):
    pass


class GameNotFinishedException(BattleshipGameException):
    pass


class PlayersAlreadyConnectedException(BattleshipGameException):
    pass
