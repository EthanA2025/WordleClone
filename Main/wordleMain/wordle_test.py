import wordle
import random

def test_get_secret_redly():
    random.seed(10)
    secret = wordle.choose_secret("Main/words/words.txt")
    assert secret == "redly"

def test_secret_correct():
    random.seed(10)
    secret = wordle.choose_secret("Main/words/words.txt")
    result = wordle.enter_guess(secret, "redly")
    assert result == -1


def test_secret_incorrect():
    random.seed(10)
    secret = wordle.choose_secret("Main/words/words.txt")
    result = wordle.enter_guess(secret, "aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    assert result == 0