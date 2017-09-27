import random

# config
low = 1
high = 100


# helper functions
def show_start_screen():
    print("▄█░ ▀█░█▀ ▄█░ 　 ▒█▀▄▀█ █▀▀ 　 ▀▀█▀▀ █░░█ █▀▀ 　 █▀▀▀ █▀▀█ █▀▄▀█ █▀▀ ░ ")
    print("░█░ ░█▄█░ ░█░ 　 ▒█▒█▒█ █▀▀ 　 ░░█░░ █▀▀█ █▀▀ 　 █░▀█ █▄▄█ █░▀░█ █▀▀   ")
    print("▄█▄ ░░▀░░ ▄█▄ 　 ▒█░░▒█ ▀▀▀ 　 ░░▀░░ ▀░░▀ ▀▀▀ 　 ▀▀▀▀ ▀░░▀ ▀░░░▀ ▀▀▀ █ ")
    print("Now with 'A.I'!")
    print()
def show_credits():
    print()
    print("▒█▀▀█ █▀▀█ █▀▀ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀▄ 　 █▀▀▄ █░░█")
    print("▒█░░░ █▄▄▀ █▀▀ █▄▄█ ░░█░░ █▀▀ █░░█ 　 █▀▀▄ █▄▄█")
    print("▒█▄▄█ ▀░▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀░ 　 ▀▀▀░ ▄▄▄█")
    print()
    print("▒█▀▄▀█ ░▀░ █▀▀▄ █▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀ ▀▀█▀▀ █░█ ░▀░ █▀▀▄ ▄█░ █▀█ █▀▀█") 
    print("▒█▒█▒█ ▀█▀ █░░█ █▀▀ █░░ █▄▄▀ █▄▄█ █▀▀ ░░█░░ █▀▄ ▀█▀ █░░█ ░█░ ░▄▀ ░░▀▄") 
    print("▒█░░▒█ ▀▀▀ ▀░░▀ ▀▀▀ ▀▀▀ ▀░▀▀ ▀░░▀ ▀░░ ░░▀░░ ▀░▀ ▀▀▀ ▀▀▀░ ▄█▄ █▄▄ █▄▄█")
    print("AKA ur mom")
    print("AKA Mr. Clean")
    print("AKA Tristan Bagwell.")
    
def get_guess(current_low, current_high):
    guess = (current_low + current_high)//2
    return guess

def pick_number():
    print("Think of a number between " + str(low) + " and " + str(high) + ". Then press enter to continue.")
    input()
    
def check_guess(guess):
    print("Is it " + str(get_guess) + "? Higher, lower, or correct?")
    check = input()
    if check == higher
        check = -1
    elif check == correct
        check = 0
    else check == lower
        check = 1
    return check

def show_result():
    print("I won! Get rekt nub!")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    check = -1
    
    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            current_low = guess
        elif check == 1:
            current_high = guess

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



