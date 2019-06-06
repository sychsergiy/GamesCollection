import random


class AbstractNumberUpdateStrategy(object):
    def get_number(self) -> int:
        raise NotImplementedError


class RandomNumberUpdateStrategy(AbstractNumberUpdateStrategy):
    def __init__(self, min_value: int, max_value: int):
        self._min_value = min_value
        self._max_value = max_value

    def get_number(self) -> int:
        return random.randint(self._min_value, self._max_value)
