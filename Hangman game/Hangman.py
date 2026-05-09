import random

# Step 1: Predefined words list
words = ["apple", "mango", "tiger", "table", "chair"]

# Step 2: Select random word
word = random.choice(words)

# Step 3: Empty guessed letters list
guessed_letters = []

# Step 4: Wrong attempts
wrong_guesses = 0
max_wrong = 6

print("🎮 Welcome to Hangman Game!")

# Step 5: Game loop
while wrong_guesses < max_wrong:

    display_word = ""

    # Show guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You won!")
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Enter only one letter.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("⚠ Already guessed.")
        continue

    guessed_letters.append(guess)

    # Check correct/wrong
    if guess not in word:
        wrong_guesses += 1
        print("❌ Wrong Guess!")
        print("Remaining chances:", max_wrong - wrong_guesses)

# Lose condition
if wrong_guesses == max_wrong:
    print("\n💀 You Lost!")
    print("Correct word was:", word)