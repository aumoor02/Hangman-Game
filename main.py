import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
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
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

stage_idx = -1
word_list = [
    "abruptly",
    "bandwagon",
    "crypt",
    "disavow",
    "embezzle",
    "fishhook",
    "galaxy",
    "injury",
    "jukebox",
    "khaki",
    "luxury",
    "microwave",
    "nightclub",
    "oxygen",
    "pajama",
    "quiz",
    "strength",
    "transcript",
    "voodoo",
    "witchcraft",
    "yummy",
    "zombie",
]
chosen_word = random.choice(word_list)

display = []

# adds a blank for each character of the chosen word
for char in chosen_word:
    display.append("_")

print("Welcome to Hangman!")
print(stages[stage_idx])

while "_" in display:
    print("")
    print(display)
    guess = input("Guess a letter: ").lower()

    # iterates through the chosen_word list, if the letter guessed was correct,
    # the display list is updated
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # displays and updates the hangman
    if guess not in display:
        print("That guess was incorrect.")
        stage_idx -= 1
        print(stages[stage_idx])

    # if the value of the negative indexing of stages == the value of the zero indx
    # the player will lose
    if stages[stage_idx] == stages[0]:
        print(f"Game over! The correct word was {chosen_word}. Please try again!")
        exit()

print(f"\nThe word was {chosen_word}")
print("Congratulations! You have Won!")
