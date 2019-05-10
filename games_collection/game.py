class AbstractGame(object):
    title = None

    def __init__(self):
        self._finished = False

    def finish(self):
        self._finished = True

    @property
    def finished(self):
        return self._finished

    def get_result_info(self) -> dict:
        raise NotImplementedError

    def __copy__(self):
        raise NotImplementedError
