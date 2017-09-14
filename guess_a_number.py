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

while guess != rand and tries < limit:
    guess = input("Take a guess: ")
    guess = int(guess)
    
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
