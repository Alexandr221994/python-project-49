from random import randint
import prompt


def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def progression():
    name = greeting()
    print('What number is missing in the progression?')
    count_true_answer = 0
    while count_true_answer < 3:
        result_list = []
        result_string = ""
        interval = randint(1, 10)
        start_number = randint(1, 50)
        count = 0

        while count < 10:
            result_list.append(start_number)
            start_number += interval
            count += 1

        random_index = randint(0, 9)

        for index, item in enumerate(result_list):
            if index == random_index:
                result_string += f'.. '
            else:
                result_string += f'{item} '

        print(f'Question: {result_string}')

        answer = prompt.string('Your answer: ')

        if int(answer) == result_list[random_index]:
            print('Correct!')
            count_true_answer += 1
        else:
            print(f"'{answer}' is wrong answer;(. Correct answer was '{result_list[random_index]}'.")
            print(f"Let's try again, {name}!")
            break

    if count_true_answer == 3:
        print(f'Congratulations, {name}!')


def main():
    progression()


if __name__ == '__main__':
    main()
