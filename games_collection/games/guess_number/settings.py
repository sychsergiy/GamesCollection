from games_collection.settings import AbstractGameSettings


class GuessNumberSettings(AbstractGameSettings):
    def __init__(self, guess_times_to_winn: int):
        self.guess_times_to_winn = guess_times_to_winn
