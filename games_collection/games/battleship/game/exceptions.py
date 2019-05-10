class BattleshipGameException(Exception):
    pass


class GameOverException(BattleshipGameException):
    pass


class PlayerNotConnectedException(BattleshipGameException):
    pass


class GameNotFinishedException(BattleshipGameException):
    pass


class PlayersAlreadyConnectedException(BattleshipGameException):
    pass
