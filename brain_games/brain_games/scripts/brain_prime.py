from random import randint
import prompt


def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def search_prime_number():
    name = greeting()
    print('Find the greatest common divisor of given numbers.')
    count_true_answer = 0

    while count_true_answer < 3:
        number = randint(1, 101)
        count = 0

        for i in range(1, number + 1):
            if number % i == 0:
                count += 1

        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if count == 2 and answer == 'yes' or count != 2 and answer == 'no':
            print('Correct!')
            count_true_answer += 1
        elif answer == 'yes':
            print('Answer "yes" if the number is prime, otherwise answer "no".')
            print(f"Let's try again, {name}!")
            break
        elif answer == 'no':
            print('Answer "no" if the number is prime, otherwise answer "yes".')
            print(f"Let's try again, {name}!")
            break
        else:
            print('Incorrect answer')
            print(f"Let's try again, {name}!")
            break

    if count_true_answer == 3:
        print(f'Congratulations, {name}!')


def main():
    search_prime_number()


if __name__ == '__main__':
    main()
