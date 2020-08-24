from random import randrange

# Checks the difficulty and also checks if the input is correct

def difficulty_check(nb_max, lowest_nb):
    x = 0
    level = input("Choose a difficulty:\nWrite 1 for easy\nWrite 2 for medium\nWrite 3 for hard\n(and so on, there are an infinite amount of levels)\n")
    if level.isdigit() == False:
        print("Wrong entry, try again")
        difficulty_check(nb_max, lowest_nb)
    nb = 1
    while x + 1 <= int(level):
        x += 1
        nb *= 10
    return (nb)

def user_nb_check(user_guess, max_nb, lowest_nb):
    user_guess = input("Guess the random number between 0 and " + str(max_nb) + " included\n")
    if user_guess.isdigit() == False:
        print("Wrong entry, try again")
        user_nb_check(user_guess, max_nb, lowest_nb)
    elif int(user_guess) > max_nb or int(user_guess) < lowest_nb:
        print("Wrong entry, try again")
        user_nb_check(user_guess, max_nb, lowest_nb)
    return (user_guess)

# For the rand_nb variable, I add zeros in front, depending of the max_nb
# and cast it as a string so it keeps the zeros

def nb_guess():
    max_nb = difficulty_check(0, 0)
    lowest_nb = 0
    user_guess = 0
    rand_nb = str("%0*d" % (len(str(max_nb)), randrange(max_nb - 1)))
    print("randint = ", rand_nb)
    user_guess = user_nb_check(str(user_guess), max_nb, lowest_nb)

nb_guess()
