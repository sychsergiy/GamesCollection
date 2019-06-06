from games_collection.game_player import AbstractGamePlayer
from games_collection.games.guess_number.counter import Counter
from games_collection.games.guess_number.settings import GuessNumberSettings

number_to_guess = 1
settings = GuessNumberSettings(2)

counter = Counter()


def update_number_to_guess():
    import random
    global number_to_guess
    number_to_guess = random.randint(0, 10)


class GuessNumberPlayer(AbstractGamePlayer):
    def turn(self, number: int):
        global number_to_guess
        if number == number_to_guess:
            counter.increment_guesses()
            update_number_to_guess()
            return True
        else:
            counter.increment_misses()
            return False
