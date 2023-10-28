import random
from data import stages, word_list
from colorama import init
from termcolor import colored
from pyfiglet import Figlet


f = Figlet(font="big")
init()


stage_idx = -1

chosen_word = random.choice(word_list)

display = []

# adds a blank for each character of the chosen word
for char in chosen_word:
    display.append("_")

print(f.renderText("Hangman!"))
print(colored(stages[stage_idx], "blue"))

while "_" in display:
    print("")
    print(display)
    guess = input(colored("Guess a letter: ", "green")).lower()

    # iterates through the chosen_word list, if the letter guessed was correct,
    # the display list is updated
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # displays and updates the hangman
    if guess not in display:
        print(colored("That guess was incorrect.", "red"))
        stage_idx -= 1
        print(colored(stages[stage_idx], "blue"))

    # if the value of the negative indexing of stages == the value of the zero indx
    # the player will lose
    if stages[stage_idx] == stages[0]:
        print(
            colored(
                f"Game over! The correct word was {chosen_word}. Please try again!",
                "red",
            )
        )
        exit()

print(colored(f"\nThe word was {chosen_word}", "green"))
print(colored("Congratulations! You have Won!", "green"))
