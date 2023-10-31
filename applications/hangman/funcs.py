import random as r  # importing library

wordListHard = []
wordListEasy = []
easyReadCount = 0  # initiallizing variable and dependency

with open("WordListHard.txt", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        wordListHard.append(line)
with open("WordListEasy.txt", "r") as f:
    for line in f.readlines():
        if easyReadCount % 2 == 0:
            line = line.strip('\n')
            wordListEasy.append(line)
        else:
            line = line.strip('\n')
        easyReadCount += 1  # importing dependency


def hangmanEasy():
    UIFrame = ['__________\n|        |\n|        |\n', '|        |\n', '|      ', ' ', ' |\n', '|      ', '  |\n',
               '----------']
    HangmanPicture = ['__________\n| ______ |\n|      | |\n', '|      o |\n', '|     /', '|', '\|\n', '|     /',
                      ' \|\n', '----------']
    printWords = ['_', '_', '_', '_', '_', '_', '_', '_']

    wrongAnswerCounter = 0
    guessedWords = []
    randomWordList = []

    randomWord = r.choice(wordListEasy)
    for wordLetter in randomWord:
        randomWordList.append(wordLetter.lower())  # initiallizing variable and dependency, chosing a word

    print(
        '----------------------------------------------------------------------------------------------------------------\n',
        ''.join(printWords), "\n There's 8 letter in this word",
        '\n----------------------------------------------------------------------------------------------------------------')  # Start Menu

    while printWords != randomWordList:
        wrongLetterInWordCounter = 0
        counter_a = 0
        counter_b = 0  # reseting counters

        userInput = input("Please enter your guess letter: ")
        userInput = userInput.lower()
        while len(userInput) > 1 or len(userInput) == 0:
            userInput = input("Please only enter one letter!\nPlease re-enter your guess letter: ")
        while ord(userInput) < 97 or ord(userInput) > 122:
            userInput = input("Please enter a letter!\nPlease re-enter your guess letter: ")
        while userInput in guessedWords:
            userInput = input("Please don't re-enter guessed words:")  # user input and checking

        guessedWords.append(userInput)  # recording guessed words

        while counter_a < len(randomWordList):
            if userInput == randomWordList[counter_a]:
                printWords[counter_a] = userInput
            else:
                wrongLetterInWordCounter += 1
            counter_a += 1  # matching answers

        if wrongLetterInWordCounter == 8:
            wrongAnswerCounter += 1  # counting wrong answers

        while counter_b < wrongAnswerCounter:
            UIFrame[counter_b] = HangmanPicture[counter_b]
            counter_b += 1  # remaking output ui

        if printWords == randomWordList:
            print("Congrats! You saved your man!")
            print("The word is: ", ''.join(printWords))
        elif 7 - wrongAnswerCounter != 0:
            print("The word you've guessed: ", ''.join(printWords))
            print(''.join(UIFrame))
            print("You have ", 7 - wrongAnswerCounter, " Wrong answers left.")
        elif 7 - wrongAnswerCounter == 0:
            print("YOUR MAN DIED...")
            print("The correct word is: ", randomWord)
            printWords = randomWordList  # output selection

        print(
            '----------------------------------------------------------------------------------------------------------------')  # ui frame


def hangmanHard():
    UIFrame = ['__________\n|        |\n|        |\n', '|        |\n', '|      ', ' ', ' |\n', '|      ', '  |\n',
               '----------']
    HangmanPicture = ['__________\n| ______ |\n|      | |\n', '|      o |\n', '|     /', '|', '\|\n', '|     /',
                      ' \|\n', '----------']
    printWords = []
    underline = '_'

    wrongAnswerCounter = 0
    guessedWords = []
    randomWordList = []

    randomWord = r.choice(wordListHard)
    for wordLetter in randomWord:
        randomWordList.append(wordLetter.lower())  # initiallizing variable and dependency, chosing a word
    for i in range(0, len(randomWord)):
        printWords.append(underline)
    print(
        '----------------------------------------------------------------------------------------------------------------\n',
        ''.join(printWords), "\n There's ", len(randomWord), " letter in this word",
        '\n----------------------------------------------------------------------------------------------------------------')  # Start Menu

    while printWords != randomWordList:
        wrongLetterInWordCounter = 0
        counter_a = 0
        counter_b = 0  # reseting counters

        userInput = input("Please enter your guess letter: ")
        userInput = userInput.lower()
        while len(userInput) > 1 or len(userInput) == 0:
            userInput = input("Please only enter one letter!\nPlease re-enter your guess letter: ")
        while ord(userInput) < 97 or ord(userInput) > 122:
            userInput = input("Please enter a letter!\nPlease re-enter your guess letter: ")
        while userInput in guessedWords:
            userInput = input("Please don't re-enter guessed words:")  # user input and checking

        guessedWords.append(userInput)  # recording guessed words

        while counter_a < len(randomWordList):
            if userInput == randomWordList[counter_a]:
                printWords[counter_a] = userInput
            else:
                wrongLetterInWordCounter += 1
            counter_a += 1  # matching answers

        if wrongLetterInWordCounter == len(randomWordList):
            wrongAnswerCounter += 1  # counting wrong answers

        while counter_b < wrongAnswerCounter:
            UIFrame[counter_b] = HangmanPicture[counter_b]
            counter_b += 1  # remaking output ui

        if printWords == randomWordList:
            print("Congrats! You saved your man!")
            print("The word is: ", ''.join(printWords))
        elif 7 - wrongAnswerCounter != 0:
            print("The word you've guessed: ", ''.join(printWords))
            print(''.join(UIFrame))
            print("You have ", 7 - wrongAnswerCounter, " Wrong answers left.")
        elif len(randomWordList) - 1 - wrongAnswerCounter == 0:
            print("YOUR MAN DIED...")
            print("The correct word is: ", randomWord)
            printWords = randomWordList  # output selection

        print(
            '----------------------------------------------------------------------------------------------------------------')  # ui frame


def hangmanCustom():
    UIFrame = ['__________\n|        |\n|        |\n', '|        |\n', '|      ', ' ', ' |\n', '|      ', '  |\n',
               '----------']
    HangmanPicture = ['__________\n| ______ |\n|      | |\n', '|      o |\n', '|     /', '|', '\|\n', '|     /',
                      ' \|\n', '----------']
    printWords = []
    underline = '_'

    wrongAnswerCounter = 0
    guessedWords = []
    inputWordList = []

    inputWord = input("Please input your chosen word for player 2: ")
    for wordLetter in inputWord:
        inputWordList.append(wordLetter.lower())  # initiallizing variable and dependency, chosing a word
    for i in range(0, len(inputWord)):
        printWords.append(underline)
    print(
        '\n\n\n\n\n\n\n\n\n\n\n\n\n----------------------------------------------------------------------------------------------------------------\n',
        ''.join(printWords), "\n There's ", len(inputWord), " letter in this word",
        '\n----------------------------------------------------------------------------------------------------------------')  # Start Menu

    while printWords != inputWordList:
        wrongLetterInWordCounter = 0
        counter_a = 0
        counter_b = 0  # reseting counters

        userInput = input("Please enter your guess letter: ")
        userInput = userInput.lower()
        while len(userInput) > 1 or len(userInput) == 0:
            userInput = input("Please only enter one letter!\nPlease re-enter your guess letter: ")
        while userInput in guessedWords:
            userInput = input("Please don't re-enter guessed words:")  # user input and checking

        guessedWords.append(userInput)  # recording guessed words

        while counter_a < len(inputWordList):
            if userInput == inputWordList[counter_a]:
                printWords[counter_a] = userInput
            else:
                wrongLetterInWordCounter += 1
            counter_a += 1  # matching answers

        if wrongLetterInWordCounter == len(inputWordList):
            wrongAnswerCounter += 1  # counting wrong answers

        while counter_b < wrongAnswerCounter:
            UIFrame[counter_b] = HangmanPicture[counter_b]
            counter_b += 1  # remaking output ui

        if printWords == inputWordList:
            print("Congrats! You saved your man!")

            print("The word is: ", ''.join(printWords))
        elif 7 - wrongAnswerCounter != 0:
            print("The word you've guessed: ", ''.join(printWords))
            print(''.join(UIFrame))
            print("You have ", 7 - wrongAnswerCounter, " Wrong answers left.")
        elif len(inputWordList) - 1 - wrongAnswerCounter == 0:
            print("YOUR MAN DIED...")
            print(''.join(UIFrame))
            print("The correct word is: ", inputWord)
            printWords = inputWordList  # output selection

        print(
            '----------------------------------------------------------------------------------------------------------------')  # ui frame
