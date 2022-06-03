from art import *
from game_data import data
import os
import random


def clear():
    os.system('clear')
    print(logo)


def choose_comparison():
    return random.choice(data)


def current_answer(a, b):
    if a['follower_count'] < b['follower_count']:
        return 'B'
    else:
        return 'A'


def check_guess(winning_answer, current_answer, score):
    if winning_answer == current_answer:
        clear()
        print(f"You're right! Current score: {score+1}")
        return True
    else:
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")
        return False


def get_guess(a, b):
    print(
        f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(
        f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    return user_guess


def game():
    user_score = 0
    playing = True
    clear()
    a_compare = choose_comparison()
    while playing:
        b_compare = choose_comparison()

        user_guess = get_guess(a_compare, b_compare)

        answer = current_answer(a_compare, b_compare)

        if check_guess(answer, user_guess, user_score):
            user_score += 1
            a_compare = b_compare
        else:
            playing = False


game()
