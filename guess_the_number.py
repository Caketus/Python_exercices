import random

# Checks the difficulty and also checks if the input is correct

def nb_check(nb, nb_max, lowest_nb):
    if nb == 0:
        level = input("Choose a difficulty:\nWrite 1 for easy\nWrite 2 for medium\nWrite 3 for hard\n")
        if level.isdigit() == False:
            while level.isdigit() == False:
                level = input("Wrong entry, try again\n")
        if int(level) < 1 or int(level) > 3:
            while int(level) < 1 or int(level) > 3:
                level = input("Wrong entry, try again\n")
        if int(level) == 1:
            nb = 10
        if int(level) == 2:
            nb = 100
        if int(level) == 3:
            nb = 1000
    # else:
    #     if nb > nb_max or nb < lowest_nb:

    return nb



def nb_guess():
    lowest_nb = 0
    max_nb = nb_check(0, 0, lowest_nb)
    user_guess = input("Guess the random number between 0 and " + str(max_nb) + " included\n")
    lowest_nb
    user_guess = nb_check(user_guess, max_nb, lowest_nb)


nb_guess()



# BUVER DE L'O LES AMIS
