from random import randint

OUTPUT_TASK = 'Find the greatest common divisor of given numbers.'
RANDOM_NUMBER = randint(1, 101)


def search_prime_number(number: int):
    count = 0
    for item in range(1, number + 1):
        if number % item == 0:
            count += 1
    if count != 2:
        return 'no'
    else:
        return 'yes'


def game():
    question = RANDOM_NUMBER
    correct_answer = search_prime_number(RANDOM_NUMBER)
    return question, str(correct_answer)
