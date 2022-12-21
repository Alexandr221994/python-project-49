from random import randint

OUTPUT_TASK = 'What number is missing in the progression?'


def game():
    start_number = randint(1, 50)
    interval = randint(1, 10)
    random_index = randint(0, 9)
    list_progression = list(range(start_number, start_number + interval * 10, interval))
    list_progression[random_index], correct_answer = '..', list_progression[random_index]
    question = ' '.join(list(map(str, list_progression)))
    return question, str(correct_answer)
