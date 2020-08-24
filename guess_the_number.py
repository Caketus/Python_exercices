import random

# Checks the difficulty and also checks if the input is correct

def nb_check(nb_max, lowest_nb):
    x = 0
    level = input("Choose a difficulty:\nWrite 1 for easy\nWrite 2 for medium\nWrite 3 for hard\n(and so on, there are an infinite amount of levels)\n")
    if level.isdigit() == False:
        print("Wrong entry, try again")
        nb_check(nb, nb_max, lowest_nb)
    nb = 1
    while x + 1 <= int(level):
        x += 1
        nb *= 10
    return (nb)



def nb_guess():
    max_nb = nb_check(0, 0)
    user_guess = input("Guess the random number between 0 and " + str(max_nb) + " included\n")
    lowest_nb = user_guess
    user_guess = user_nb_check(user_guess, max_nb, lowest_nb)


nb_guess()
