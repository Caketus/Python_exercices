import random

# Checks the difficulty and also checks if the input is correct

def nb_check(nb, nb_max):
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
     # else
     #     if
    return nb



def nb_guess():
    max_nb = 0
    max_nb = nb_check(max_nb, 0)
    print("el maximumo ==", max_nb)
    user_guess = input("Guess the random number between 1 and " + str(max_nb) + "\n")
    user_guess = nb_check(user_guess, max_nb)


nb_guess()



# BUVER DE L'O LES AMIS
