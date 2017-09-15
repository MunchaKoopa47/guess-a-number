import random

#Configuration
low = 1
high = 100
limit = 10

#Start criteria
rand = random.randrange(low, high)
print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

guess = -1
tries = 0

#Helper functions
def get_guess():
    while True:
        g = input("Take a guess: ")

        if g.isnumeric():
            g = int(g)
            return g
        else:
            print("You must enter a number you schweinhun!")
            
#Play game
while guess != rand and tries < limit:
    guess = get_guess()
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

    tries += 1

#Gives outcome for player
if guess == rand:
    print("Noice job m8.")
else:
    print("Git gud lmao. The number I was thinking of was " + str(rand) + " you scrub.")
