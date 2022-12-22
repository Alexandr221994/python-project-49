from random import randint

OUTPUT_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int):
    return number % 2 == 0


def get_game():
    question: int = randint(0, 100)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, str(correct_answer)
