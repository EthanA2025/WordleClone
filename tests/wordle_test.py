from src.wordle import choose_secret, enter_guess
import random

def test_get_secret_redly():
    random.seed(10)
    secret = choose_secret("words/words.txt")
    assert secret == "redly"

def test_secret_correct():
    random.seed(10)
    secret = choose_secret("words/words.txt")
    result = enter_guess(secret, "redly")
    assert result == True


def test_secret_incorrect():
    random.seed(10)
    secret = choose_secret("words/words.txt")
    result = enter_guess(secret, "falsee")
    assert result == False