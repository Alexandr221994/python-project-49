from random import randint

OUTPUT_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def search_prime_number(number: int):
    count = 0
    for item in range(1, number + 1):
        if number % item == 0:
            count += 1
    return count == 2


def game():
    question = randint(1, 101)
    if search_prime_number(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, str(correct_answer)
