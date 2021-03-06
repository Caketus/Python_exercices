# Create a program that will play the “cows and bulls” game with the user.
# The game works like this:
# Randomly generate a 4-digit number.
# Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the
# correct place, they have a “cow”. For every digit the
# user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how
# many “cows” and “bulls” they have. Once the user guesses
# the correct number, the game is over. Keep track of the
# number of guesses the user makes throughout the game and
# tell the user at the end.

import random

def verify_entry():
    user_digits = input("Just write a 4 digits number : \n")
    if len(user_digits) != 4:
        print("We need EXACTLY 4 digits !")
        user_digits = verify_entry()
    if user_digits.isdigit() == False:
        print("I SAID DIGITS ! :\n")
        user_digits = verify_entry()
    return user_digits

def compare_digits(user_digits, solution):
    cows = 0
    bulls = 0
    x = 0
    y = 0
    while x <= len(solution) - 1:
        if solution[x] == user_digits[x]:
            cows += 1
            bulls -= 1
            print("lol")
        x += 1
    while y <= len(solution) - 1:
        x = 0
        while x <= len(user_digits) - 1:
            if solution[y] == user_digits[x]:
                bulls += 1
                print("FERME TA GUEULE DAVID")
            x += 1
        y += 1
    x = 0
    while x < len(user_digits):
        y = 0
        while y < len(user_digits):
            if x != y and user_digits[x] == solution[y] and user_digits[y] == solution[y]:
                bulls -= 1
            y += 1
        x += 1
    return (cows, bulls)

def cows_and_bulls():
    user_digits = verify_entry()
    solution = "2020" # format(random.randint(0000,9999), '04d')
    cows, bulls = compare_digits(user_digits, solution)
    print("Solution = ", solution)
    print("cows ==", cows)
    print("bulls ==", bulls)


cows_and_bulls()

# user 0202
# prog 2020
