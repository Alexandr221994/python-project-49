#!/usr/bin/env python3
from random import randint
import prompt


def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def parity_check():
    name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        random_number = randint(0, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if (random_number % 2 == 0 and answer == 'yes') \
                or (random_number % 2 != 0 and answer == 'no'):
            print('Correct!')
            count += 1
        elif answer == 'yes':
            print('Answer "yes" if the number is even, otherwise answer "no".')
            print(f"Let's try again, {name}!")
            break
        elif answer == 'no':
            print('Answer "no" if the number is even, otherwise answer "yes".')
            print(f"Let's try again, {name}!")
            break
        else:
            print('Incorrect answer')
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


def main():
    parity_check()


if __name__ == '__main__':
    main()
