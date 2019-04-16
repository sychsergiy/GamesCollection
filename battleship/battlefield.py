class Battlefield(object):
    def __init__(self, size: int):
        self.size = size
        self._battlefield = [[''] * size] * size

    @property
    def battlefield(self) -> list:
        return self._battlefield
