import random

from hangman_words import word_list
from hangman_art import stages, logo
lives = 6

print(logo)
chosen_word = random.choice(word_list)
# print(chosen_word)  #Uncomment If you want to do Tracing 

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # print(chosen_word)

    if guess in correct_letters:
        print(f"\nYou've already guessed {guess}.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"\nYou guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print(f"\n***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("\n****************************YOU WIN****************************")

    print(stages[lives])
