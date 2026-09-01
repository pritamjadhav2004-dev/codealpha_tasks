import random

words = ["apple", "mango", "python", "tiger", "india"]

secret_word = random.choice(words)

guessed_letters = []

wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_wrong_guesses:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word = display_word + letter + " "
        else:
            display_word = display_word + "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses = wrong_guesses + 1
        print("Wrong guess!")
        print("Remaining chances:", max_wrong_guesses - wrong_guesses)

if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The word was:", secret_word)
