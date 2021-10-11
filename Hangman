import random

hangman1 = [
"""
+---+
    |
    |
    |
    ===""", """
+---+
  | |
  O |
    |
    ===""", """
+---+
  | |
  O |
 /| |
    ===""", """
+---+
  | |
  O |
 /|\|
    ===""", """
+---+
  | |
  O |
 /|\|
  |  ===""", """
 / 
+---+
  | |
  O |
 /|\|
  |  ===""", """
 / \
"""
]

animals = ['tiger', 'lion', 'giraffe', 'zebra', 'dolphin', 'shark', 'elephant', 'rhino']

word = random.choice(animals).lower()


guessed_correctly = []
guessed_incorrectly = []
tries = 6
hangman_count = -1
while tries > 0:
    output = ''
    for letter in word:
        if letter in guessed_correctly:
            output += letter
        else:
            output += '_ '
    if output == word:
        break
    print("Guess the word: ",output)
    print(tries," chances left")
    guess = input().lower()
    if guess in guessed_correctly or guess in guessed_incorrectly:
        print("Already guessed", guess)
    elif guess in word:
        print("Awesome Job! You guessed the correct letter!")
        guessed_correctly.append(guess)
    else:
        print("Sorry! You have guessed a wrong letter!")
        hangman_count = hangman_count + 1
        tries = tries-1
        guessed_incorrectly.append(guess)
        print(hangman1[hangman_count])

if tries>0:
    print("You guessed it right and you win!!!")
else:
    print("Sorry you guessed the wrong letter. Try again.")

