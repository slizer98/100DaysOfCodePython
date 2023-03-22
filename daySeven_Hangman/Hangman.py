import random
from hangman_art import stages, logo
from hangman_words import word_list
chosen_word = random.choice(word_list)
lives = 6

size_word = len(chosen_word)
display = []

for _ in range(size_word):
    display.append('_')

game_over = False
print(logo)
while not game_over :
    guess = input("Guess a letter: ").lower()


    for position in range(size_word):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
    print(stages[lives])

    print(f'{" ".join(display)}')
    if "_" not in display:
        print('You win')
        game_over = True
     

    if lives <= 0:
        print('You lose')
        print(f'The word was {chosen_word}')
        game_over = True