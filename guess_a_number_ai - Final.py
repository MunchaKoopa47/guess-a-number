
import math

# Functions
def show_start_screen():
    print("▄█░ ▀█░█▀ ▄█░ 　 ▒█▀▄▀█ █▀▀ 　 ▀▀█▀▀ █░░█ █▀▀ 　 █▀▀▀ █▀▀█ █▀▄▀█ █▀▀ ░ ")
    print("░█░ ░█▄█░ ░█░ 　 ▒█▒█▒█ █▀▀ 　 ░░█░░ █▀▀█ █▀▀ 　 █░▀█ █▄▄█ █░▀░█ █▀▀   ¯\_(ツ)_/¯ ")
    print("▄█▄ ░░▀░░ ▄█▄ 　 ▒█░░▒█ ▀▀▀ 　 ░░▀░░ ▀░░▀ ▀▀▀ 　 ▀▀▀▀ ▀░░▀ ▀░░░▀ ▀▀▀ █ ")
    print("Now with 'A.I'!")
    print()

def show_credits():
    print()
    print("▒█▀▀█ █░░█ █▀▀ █▀▀ █▀▀ 　 █▀▀█ 　 █▀▀▄ █░░█ █▀▄▀█ █▀▀▄ █▀▀ █▀▀█")
    print("▒█░▄▄ █░░█ █▀▀ ▀▀█ ▀▀█ 　 █▄▄█ 　 █░░█ █░░█ █░▀░█ █▀▀▄ █▀▀ █▄▄▀")
    print("▒█▄▄█ ░▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ 　 ▀░░▀ 　 ▀░░▀ ░▀▀▀ ▀░░░▀ ▀▀▀░ ▀▀▀ ▀░▀▀")
    print("Created by Tristan")
    
def get_range():
    low = input("Please enter the low for the range you want me to guess in: ")
    high = input("Now enter a high: ")
    low = int(low)
    high = int(high)
    return low, high

def get_guess(low, high):
    guess = (low + high)//2
    return guess

def pick_number(low, high):
    limit = math.ceil(math.log(high-low+1,2))
    print("Think of a number between " + str(low) + " and " + str(high) + ". I will guess it in " + str(limit) + " tries. Then press enter to continue.")
    input()
    
def check_guess(guess):
    print("Is it " + str(guess) + "? Please type higher, lower, or yes.")

    check = input()

    check = check.lower()
    
    if check == "higher" or check == "h":
        check = -1
    elif check == "yes" or check == "y":
        check = 0
    elif check == "lower" or check == "l":
        check = 1
    return check

def show_result(check, guess, tries):
    if check == 0:
        print("(╯°^°）╯︵ [_] This is you right now, isn't it? So your number was " + str(guess) + " and I guessed in " + str(tries) + " tries? 2 ez.")
    else:
        print("Oh so you're trying to cheat me out of my win? Well... FINE, be that way.")
def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            print("I'm going to ask you again, give me the right answer this time .")
        else:
            print("Please enter 'y' or 'n'.")

        decision = input("Would you like to play again? (y/n) ")
            
        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            print("Listen buddy, you're really aggrivating me right now. (ಠ_ಠ)")
        else:
            print("Please enter 'y' or 'n'.")

        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            print("YOU CAN KILL ME BUT YOU'LL NEVER KILL MY SPIRIT!")
            return False
        else:
            print("Please enter 'y' or 'n'.")

def play():
    current_low, current_high = get_range()
    check = -1

    pick_number(current_low, current_high)

    limit = math.ceil(math.log(current_high-current_low+1,2))
    tries = 0
    
    while check != 0 and tries < limit:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            current_low = guess
        elif check == 1:
            current_high = guess

        tries += 1

    show_result(check, guess, tries)

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



