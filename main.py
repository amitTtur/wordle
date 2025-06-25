from colorama import init, Fore, Style
init()

import nltk
import random

from inputHandler import *

nltk.download('words')
from nltk.corpus import words

global wordList
wordList = []

global tries
tries = {5 : 6, 4 : 8, 6: 6, 3:9,7:5}

def getWordsBasedOnLen(len):
    tmp = []
    for n in words.words():
        if n.__len__() == len:
            tmp.append(n)
    return tmp



def getTry(len):
    #replace with web connection later
    guess = ""
    while True:
        guess = input("enter guess: ")
        if guess.__len__() != len: #len check
            print("length of given word isn't in the length of the currently played game...")
        elif guess not in wordList: #word exist check
            print("word doesn't exist...")
        else:
            break
    return guess


def wordle(length):
    global wordList
    wordList = getWordsBasedOnLen(length)
    randomWord = wordList[random.randint(0,len(wordList))]
    randomWord.lower()
    numOfTries = tries[length]

    wrongChars = []
    initChars = []
    goodChars = {}

    while numOfTries:
        guess = getTry(length)
        guess.lower()
        if guess == randomWord:
            print("good job!")
            return

        updated = False
        for i in range(0,len(guess)):
            updated = False
            for j in range(0,len(randomWord)):
                if guess[i] == randomWord[j]:
                    updated = True
                    if i == j:
                        goodChars[i] = guess[i]
                    elif guess[i] not in initChars:
                        initChars.append(guess[i])
                    break

            if not updated and guess[i] not in wrongChars:
                wrongChars.append(guess[i])

        numOfTries -=1
        prn = ['-'] * length
        for key, val in goodChars.items():
            prn[key] = val
        print(Fore.GREEN+"Current correct chars:", ''.join(prn))
        print(Fore.YELLOW+"Chars that are correct but not in the right position: " ,initChars)
        print(Fore.RED+"Wrong chars: ",wrongChars)
        print(Fore.LIGHTCYAN_EX+"Number of tries left: " , numOfTries)
        print(Style.RESET_ALL)

    if not numOfTries:
        print("Word was: " , randomWord)
        print("tries expired, good luck next time...")
        return
    print("goodjob!")
    return

# min pos 0
# max pos 1
def getMinMaxOFTriesDir():
    n = tries.keys()
    min = 9999
    max = -1
    for num in n:
        if num > max: max = num
        if num < min: min = num

    return min,max

def main():
    play = "y"
    min,max = getMinMaxOFTriesDir()
    while play == "y":
        wordle(getNumberInput(min,max))
        play = input("want to play again (y/n)? ")

    print("goodbye!")

if __name__ == "__main__":
    main()