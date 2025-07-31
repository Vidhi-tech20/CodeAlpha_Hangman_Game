import random

# Predefined list of 5 words
word_list = ["apple", "banana", "grape", "mango", "peach"]
secret_word = random.choice(word_list)

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Create a hidden version of the word with underscores
display_word = ["_" for _ in secret_word]

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 chances to guess wrong.")

while incorrect_guesses < max_guesses and "_" in display_word:
    print("\nCurrent word: " + " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! You have {max_guesses - incorrect_guesses} tries left.")

# Game Over
if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n💀 Game Over! The word was:", secret_word)
