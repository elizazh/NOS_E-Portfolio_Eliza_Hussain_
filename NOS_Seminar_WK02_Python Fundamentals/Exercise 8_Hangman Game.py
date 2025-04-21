import random


def hangman():
    word_list = ["python", "java", "javascript"]
    word = random.choice(word_list)
    guessed = ["_"] * len(word)
    max_guesses = 6
    attempts = 0
    guessed_letters = []

    print(" ".join(guessed))

    while attempts < max_guesses and "_" in guessed:
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)

        if guess in word:
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed[idx] = guess
        else:
            attempts += 1
            print(f"Wrong guess! {max_guesses - attempts} attempts left.")

        print(" ".join(guessed))

    if "_" not in guessed:
        print(f"Congratulations, you guessed the word '{word}'!")
    else:
        print(f"Game over! The word was '{word}'.")


# Start the game
hangman()
