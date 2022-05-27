from hangman_stages import stages, logo
from hangman_words import word_list
import random

chosen_word = random.choice(word_list)
lives = 6
print(logo)
display = ['_' for _ in chosen_word]
while "_" in display:

    guess = input("Guess a letter: ").lower()
    k = 0
    for letter in chosen_word:
        if letter == guess:
            display[k] = guess
        k += 1
    if guess not in chosen_word:
        lives -= 1
        kr = -6+lives
        if kr < -7:
            exit('You Lose')
        print('You guessed a letter that\'s not in the word, you lose a life')
        print(stages[kr])
    else:
        print(f"You have already guessed {guess}")
    print(display)

print("You Win")
