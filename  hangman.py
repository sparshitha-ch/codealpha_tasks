
import random

def play_hangman():
    words = ["python", "computer", "program", "science", "network"]
    secret_word = random.choice(words)
    guessed_letters = set()
    attempts_left = 6

    print("\n🎮 Welcome to Hangman Game!")
    print("Guess the secret word one letter at a time.")
    print(f"You have {attempts_left} incorrect guesses allowed.")

    while attempts_left > 0:
        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )
        print("\nWord:", display_word)
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) or "None")
        print("Attempts left:", attempts_left)

        if all(letter in guessed_letters for letter in secret_word):
            print("🎉 Congratulations! You guessed the word:", secret_word)
            return

        guess = input("Enter one letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("✅ Correct guess!")
        else:
            attempts_left -= 1
            print("❌ Incorrect guess!")

    print("\nGame over! The word was:", secret_word)


if __name__ == "__main__":
    play_hangman()
    