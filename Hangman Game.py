import random
def hangman_game():
    words = ["python", "intern", "coding", "alpha", "project"]
    chosen_word = random.choice(words).lower()
    word_display = ["_" for _ in chosen_word]
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have a maximum of 6 incorrect guesses.")
    print("Current word: " + " ".join(word_display))

    while incorrect_guesses < max_incorrect_guesses and "_" in word_display:
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue
        guessed_letters.append(guess)
        if guess in chosen_word:
            print(f"Good guess! '{guess}' is in the word.")
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    word_display[i] = guess
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word. You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses remaining.")
        print("Current word: " + " ".join(word_display))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
    if "_" not in word_display:
        print("\nCongratulations! You guessed the word:")
        print("".join(word_display))
        print("You won!")
    else:
        print("\nGame Over! You ran out of guesses.")
        print(f"The word was: {chosen_word}")
        print("You lost.")
if __name__ == "__main__":
    hangman_game()