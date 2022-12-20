from random import randint

OUTPUT_TASK = 'What number is missing in the progression?'
START_NUMBER = randint(1, 50)
INTERVAL = randint(1, 10)
RANDOM_INDEX = randint(0, 9)


def game():
    list_progression = list(range(START_NUMBER, START_NUMBER + INTERVAL * 10, INTERVAL))
    list_progression[RANDOM_INDEX], correct_answer = '..', list_progression[RANDOM_INDEX]
    question = ' '.join(list(map(str, list_progression)))
    return question, str(correct_answer)
