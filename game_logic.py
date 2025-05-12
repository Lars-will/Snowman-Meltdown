from ascii_art import  STAGES
import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def letter_in_secret_word(secret_word, guess):
    """Check if the guess is in the secret word."""
    if guess in secret_word:
        return True
    return False


def has_won(secret_word, guessed_letters):
    """Check if the player has won the game."""
    guessed_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            guessed_word += letter
    if guessed_word == secret_word:
        return True
    return False


def play_game():
    """Main game loop."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        # Prompt user for one guess (logic to be enhanced later)
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
        if letter_in_secret_word(secret_word, guess):
            guessed_letters.append(guess)
            if not has_won(secret_word, guessed_letters):
                print("Well done the letter exists!")
        else:
            mistakes +=1
            print("Wrong!!!")
        if has_won(secret_word, guessed_letters):
            print("Well done, the snowman lives on!")
            break
        if mistakes > 3:
            print("You lost! The snowman is no more!")
            break


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


if __name__ == "__main__":
    play_game()