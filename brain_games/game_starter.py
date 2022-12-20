from brain_games.cli import welcome_user
import prompt


def run_game(game):
    name_player = welcome_user()
    print(game.OUTPUT_TASK)
    count_true_answer = 0
    while count_true_answer < 3:
        question, correct_answer = game.game()
        print(f'Question: {question}')
        player_answer = prompt.string('Your answer: ')
        if player_answer != correct_answer:
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name_player}!")
            return
        else:
            print('Correct!')
            count_true_answer += 1
    print(f'Congratulations, {name_player}!')
