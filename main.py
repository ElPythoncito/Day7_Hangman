# --------------------------------------------MODULES
import random
from hangman_words import word_list
from hangman_art import logo, stages
# ------------------------------------------List

#-------------------------------------------Random word
print(logo)
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)
# -------------------------------------------
placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(f"Word to guess: {placeholder}")

# ----------------------------------------------While loop
game_over = False
all_words = []

while not game_over:
    print(f"**************************************** {lives}/6 LIVES **************************************************")
    guess = input("Guess a letter: ").lower()

    if guess in all_words:
        print(f"You have already guessed {guess}.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            all_words.append(letter)
        elif letter in all_words:
            display += letter
        else:
            display += "_"

    print(f"Word to guess: {display}")

    if guess not in chosen_word:
        lives -= 1
        print(f"You have guessed {guess}, but that's incorrect. You lose a life.")
        if lives == 0:
            game_over = True
            print(
                f"**************************************** IT WAS {chosen_word}! YOU LOSE 😪 **************************************************")

    if "_" not in display:
        game_over = True
        print(
            f"**************************************** YOU WIN 🎊🎊🎊 **************************************************")
    print(stages[lives])

input("\n\nType ENTER to finish!!!!")
