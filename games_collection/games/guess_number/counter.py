class Counter(object):
    def __init__(self, guesses: int = 0, misses: int = 0):
        self._guesses = guesses
        self._misses = misses

    def increment_guesses(self):
        self._guesses += 1

    def increment_misses(self):
        self._misses += 1

    @property
    def misses(self) -> int:
        return self._misses

    @property
    def guesses(self) -> int:
        return self._guesses
