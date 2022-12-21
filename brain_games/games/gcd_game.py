from random import randint
from math import gcd

OUTPUT_TASK = 'Find the greatest common divisor of given numbers.'


def game():
    first_number = randint(1, 999)
    second_number = randint(1, 999)
    correct_answer: str = gcd(first_number, second_number)
    question: str = f'Question: {first_number} {second_number}'
    return question, str(correct_answer)
