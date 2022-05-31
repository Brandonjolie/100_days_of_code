############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
import random
import os
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


def deal_card():
    return random.choice(cards)


def display(playercards, playerscore, computerfirst):
    print(
        f"    Your cards: {playercards}, current score: {playerscore}")
    print(f"    Computer's first card: {computerfirst[0]}")


def play_game():
    playing = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    while playing == 'y':
        os.system('clear')
        print(logo)
        player_cards = [deal_card(), deal_card()]
        computers_cards = [deal_card(), deal_card()]
        print(f"    Your cards: {player_cards}")
        print(f"    Computer's first card: {computers_cards[0]}")
        still_dealing = True
        if sum(player_cards) == 21:
            still_dealing = False
        while still_dealing:
            another_card = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            current_score = sum(player_cards)
            if another_card == 'y':
                player_cards.append(deal_card())
                current_score = sum(player_cards)
                if current_score > 21 and 11 in player_cards:
                    player_cards[player_cards.index(11)] = 1
                    display(player_cards, current_score, computers_cards)
                elif current_score > 21:
                    still_dealing = False
                else:
                    display(player_cards, current_score, computers_cards)
            if another_card == 'n':
                still_dealing = False
                computer_total = sum(computers_cards)
                while computer_total <= 16:
                    computers_cards.append(deal_card())
                    if computer_total > 21 and 11 in computers_cards:
                        computers_cards[computers_cards.index(11)] = 1
                    computer_total = sum(computers_cards)

        player_total = sum(player_cards)
        computer_total = sum(computers_cards)
        print(
            f"    Your final hand: {player_cards}, final score: {player_total}")
        print(
            f"    Computer's final hand: {computers_cards}, final score: {computer_total}")
        if player_total == 21 == computer_total:
            print('Draw')
        elif player_total == 21:
            print('You win 🙌🏼')
        elif player_total > computer_total and player_total <= 21:
            print('You win 🙌🏼')
        elif player_total > computer_total and player_total > 21:
            print('You lose ☹️')
        elif computer_total > player_total and computer_total <= 21:
            print('You lose ☹️')
        elif player_total < computer_total:
            print('You lose ☹️')
        playing = input(
            "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()


play_game()
