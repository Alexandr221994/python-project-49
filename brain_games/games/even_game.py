from random import randint

OUTPUT_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(hidden_number: int):
    if hidden_number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def game():
    question: int = randint(0, 100)
    correct_answer: str = is_even(question)
    return question, str(correct_answer)
