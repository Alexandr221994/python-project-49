from math import gcd
from random import randint
import prompt


def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def search_gcd():
    count = 0
    name = greeting()
    print('Find the greatest common divisor of given numbers.')
    while count < 3:
        first_number = randint(1, 999)
        second_number = randint(1, 999)
        least_common_divisor = gcd(first_number, second_number)
        print(f'Question: {first_number} {second_number}')
        answer = prompt.string('Your answer: ')
        if int(answer) == least_common_divisor:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer;(. Correct answer was '{least_common_divisor}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


def main():
    search_gcd()


if __name__ == '__main__':
    main()
