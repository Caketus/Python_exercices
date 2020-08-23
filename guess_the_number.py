import random

def difficulty_check(max_nb):
    level = input("Choose a difficulty:\nWrite 1 for easy\nWrite 2 for medium\nWrite 3 for hard\n")
    print("level ==", level)
    if level.isdigit() == False:
        print("Wrong entry, try again\n")
        if max_nb == '\0':
            difficulty_check()
    if int(level) < 1 or int(level) > 3:
        print("Wrong entry, try again\n")
        if max_nb == '\0':
            difficulty_check()
    if level == "1":
        level = 10
    if level == "2":
        level = 100
    if level == "3":
        level = 1000
    return level



def nb_guess():
    max_nb = int(difficulty_check(max_nb))
    user_gess = input("Guess the random number between 1 and ", max_nb)

nb_guess()



# jvm les amis
# jvm les amis
# jvm les amis
# jvm les amis
# jvm les amis
# jvm les amis
# jvm les amis
