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
    print("Think of a number" + low + " to " + high + ". I will try to guess.")
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
    """
    Return a truncated average of current low and high.
    """
    pass

def pick_number():
    """
    Ask the player to think of a number between low and high.
    Then  wait until the player presses enter.
    """
    pass

def check_guess(guess):
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """

def show_result():
    """
    Says the result of the game. (The computer might always win.)
    """
    pass

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
            # adjust current_low
            pass
        elif check == 1:
            # adjust current_high
            pass

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



