"""
Text-based Hangman Game in Python
Simplified Scope:
● Use a small list of 5 predefined words (no need to use a file or API).
● Limit incorrect guesses to 6.
● Basic console input/output — no graphics or audio.
Key Concepts Used: random, while loop, if-else, strings, lists.
"""

import random

# Concept: LISTS — 5 predefined words
WORDS = ["PYTHON", "REACT", "HANGMAN", "ALGORITHM", "DEVELOPER"]

MAX_INCORRECT_GUESSES = 6

# ASCII text representations of the hangman stages (0 to 6 mistakes)
HANGMAN_STAGES = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]


def play_hangman(secret_word=None):
    print("=" * 50)
    print("         TEXT-BASED HANGMAN (PYTHON EDITION)       ")
    print("=" * 50)

    # Concept: RANDOM — choose randomly from the 5 predefined words
    if secret_word is None:
        secret_word = random.choice(WORDS)

    # Concept: LISTS — tracking letters guessed by the player
    guessed_letters = []
    incorrect_guesses = 0

    print(f"Word selected at random ({len(secret_word)} letters). Max incorrect guesses: {MAX_INCORRECT_GUESSES}.")
    print("Type a single letter [A-Z] and press Enter.\n")

    # Concept: WHILE LOOP — continues until 6 mistakes or all letters guessed
    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        # Concept: STRINGS & LISTS — format the masked word display
        masked_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])

        print(HANGMAN_STAGES[incorrect_guesses])
        print(f"Word: {masked_word}")
        print(f"Attempts remaining: {MAX_INCORRECT_GUESSES - incorrect_guesses} / {MAX_INCORRECT_GUESSES}")
        if guessed_letters:
            print(f"Guessed letters: {', '.join(guessed_letters)}")

        # Check win condition: every letter in secret_word has been guessed
        if all(letter in guessed_letters for letter in secret_word):
            print("\n" + "=" * 50)
            print(f"VICTORY! You guessed the word '{secret_word}' correctly!")
            print("=" * 50)
            return True

        # Input handling
        try:
            guess = input("\nGuess a letter: ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            print("\nGame exited.")
            return False

        # Concept: IF-ELSE — input validation & branch checking
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("(!) Invalid input. Please enter exactly one alphabetical letter (A-Z).")
            continue

        if guess in guessed_letters:
            print(f"(!) You already guessed '{guess}'. Try another letter!")
            continue

        # Append valid guess to the list
        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"\n(+) Good job! '{guess}' is in the word!")
        else:
            incorrect_guesses += 1
            print(f"\n(-) Sorry! '{guess}' is not in the word.")

    # Limit of 6 incorrect guesses reached
    print(HANGMAN_STAGES[6])
    print("\n" + "=" * 50)
    print("GAME OVER! You ran out of attempts.")
    print(f"The secret word was: '{secret_word}'")
    print("=" * 50)
    return False


if __name__ == "__main__":
    while True:
        play_hangman()
        try:
            play_again = input("\nPlay again? (y/n): ").strip().lower()
            if play_again not in ("y", "yes"):
                print("Thanks for playing Hangman! Goodbye.")
                break
        except (EOFError, KeyboardInterrupt):
            break