import random

words = ["python", "coding", "github", "rocket"]
word = random.choice(words)
attempts = 6
guessed = []
display = []

for i in word:
    display.append("_")

print("Welcome to the Word Guessing Game!")

while attempts > 0:
    print("\nWord: ", end="")
    for letter in display:
        print(letter, end=" ")
    print("\nAttempts Left:", attempts)
    print("Guessed letters:", guessed)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1:
        print("Enter only one letter.")
        continue
    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)
    found = False

    for i in range(len(word)):
        if word[i] == guess:
            display[i] = guess
            found = True

    if found:
        print("Correct Guess!")
    else:
        print("Wrong Guess!")
        attempts = attempts - 1

    win = True
    for letter in display:
        if letter == "_":
            win = False
    if win:
        print("\nYou Won!")
        print("Word was:", word)
        break

if attempts == 0:
    print("\nGame Over!")
    print("Word was:", word)
    