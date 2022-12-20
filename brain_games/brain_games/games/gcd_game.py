from random import randint
from math import gcd

OUTPUT_TASK = 'Find the greatest common divisor of given numbers.'
FIRST_NUMBER = randint(1, 999)
SECOND_NUMBER = randint(1, 999)


def game():
    correct_answer: str = gcd(FIRST_NUMBER, SECOND_NUMBER)
    question: str = f'Question: {FIRST_NUMBER} {SECOND_NUMBER}'
    return question, str(correct_answer)
