from random import randint, choice

MATH_OPERATORS = ['+', '-', '*']
MIN_NUMBER = 1
MAX_NUMBER = 99
OUTPUT_TASK = 'What is the result of the expression?'


def calculate(operator: str, first_number: int, second_number: int):
    if operator == '+':
        return first_number + second_number
    if operator == '-':
        return first_number - second_number
    if operator == '*':
        return first_number * second_number


def game():
    first_number: int = randint(MIN_NUMBER, MAX_NUMBER)
    second_number: int = randint(MIN_NUMBER, MAX_NUMBER)
    operator = choice(MATH_OPERATORS)
    question: str = f'{first_number} {operator} {second_number}'
    correct_answer: int | str = calculate(operator, first_number, second_number)
    return question, str(correct_answer)
