#2 Hangman Game
from random import *
words = ["apple", "bananna", "orange"]
word = choice(words)
print("answer : "+ word)
letters = ""

while True:
    succed = True
    print()
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succed = False
    print()

    if succed:
        print("Success")
        break
    
    letter = input("Input letter > ")
    if letter not in letters:
        letters += letter

    if letter in word:
        print("correct")
    else:
        print("wrong")