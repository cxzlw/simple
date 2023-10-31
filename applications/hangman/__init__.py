from . import funcs

title = "Hangman 101"
description = "Both challenging and fun game where you need to save your poor man!"


def main():
    userChoice = input("There are three gamemodes, easy, hard, and custom.\nPlease choose your gamemode:")
    if userChoice.lower() == 'easy':
        funcs.hangmanEasy()
    elif userChoice.lower() == 'hard':
        funcs.hangmanHard()
    elif userChoice.lower() == 'custom':
        funcs.hangmanCustom()
    else:
        print("I don't understand you...\nPlease restart the programme")
