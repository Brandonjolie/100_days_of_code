from art import logo
import random
EASY = 10
HARD = 5


def welcome():
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")


def guess_again(turns_left):
    if turns_left > 0:
        print('Guess again.')


def game():
    welcome()
    answer = random.randint(1, 100)
    options = {'easy': EASY, 'hard': HARD}
    difficulty = options[input("Choose a difficulty. Type 'easy' or 'hard': ")]
    print(logo)
    print(answer)
    while difficulty != 0:
        print(f'You have {difficulty} attempts remaining to guess the number.')
        choice = int(input('Make a guess: '))
        if choice < answer:
            difficulty -= 1
            guess_again(difficulty)
        elif choice > answer:
            difficulty -= 1
            guess_again(difficulty)
        elif choice == answer:
            print(f'You got it! The answer was {answer}')
            break
    print('You\'ve run out of attempts, you lose')


game()
