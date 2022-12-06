#!/usr/bin/env python3
from random import randint
import prompt


def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def calc():
    count = 0
    name = greeting()
    print('What is the result of the expression?')
    while count < 3:
        first_number = randint(0, 100)
        second_number = randint(0, 100)
        operation = randint(0, 2)
        if operation == 0:
            result_string = f'Question: {first_number} + {second_number}'
            result_operation = first_number + second_number
        elif operation == 1:
            result_string = f'Question: {first_number} - {second_number}'
            result_operation = first_number - second_number
        else:
            result_string = f'Question: {first_number} * {second_number}'
            result_operation = first_number * second_number
        print(result_string)
        answer = prompt.string('Your answer: ')
        if int(answer) == result_operation:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer;(. Correct answer was '{result_operation}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


def main():
    calc()


if __name__ == '__main__':
    main()
