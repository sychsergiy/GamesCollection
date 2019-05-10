class BattleshipPlayerException(Exception):
    pass


class PlayerNotConnectedToGameException(BattleshipPlayerException):
    pass


class OpponentNotConnectedToGameException(BattleshipPlayerException):
    pass


class PlayerShipsNotLocatedException(BattleshipPlayerException):
    pass


class OpponentShipsNotLocatedException(BattleshipPlayerException):
    pass

