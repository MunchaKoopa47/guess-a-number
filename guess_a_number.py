import random
import math

# config
low = 1
high = 100

# helper functions
def show_start_screen():
    print("▄█░ ▀█░█▀ ▄█░ 　 ▒█▀▄▀█ █▀▀ 　 ▀▀█▀▀ █░░█ █▀▀ 　 █▀▀▀ █▀▀█ █▀▄▀█ █▀▀ ░ ")
    print("░█░ ░█▄█░ ░█░ 　 ▒█▒█▒█ █▀▀ 　 ░░█░░ █▀▀█ █▀▀ 　 █░▀█ █▄▄█ █░▀░█ █▀▀ ▄ ")
    print("▄█▄ ░░▀░░ ▄█▄ 　 ▒█░░▒█ ▀▀▀ 　 ░░▀░░ ▀░░▀ ▀▀▀ 　 ▀▀▀▀ ▀░░▀ ▀░░░▀ ▀▀▀ █ ")
    print()
    print("You get " + str(limit) + " tries to guess.")
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
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("U must enter a number ya nub.")

def pick_number():
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +".")

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

def show_result(guess, rand):
    if guess == rand:
        print("Noice job m8!")
    else:
        print("Git gud lmao. Ur a skrub. The number was " + str(rand) + ".")

def play_again():
    while True:
        decision = input("Wanna 1v1 me again? Insert credit to continue.")

        decision = decision.lower()

        if decision == 'credit':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'credit' or 'n' or 'no'.")

def play():
    guess = -1
    tries = 0
    limit = round(math.log(high-low+1,2))

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
