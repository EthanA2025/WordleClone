import wordle
import random

def test_get_secret_redly():
    random.seed(10)
    secret = wordle.chooseSecret("words/words.txt")
    assert secret == "redly"