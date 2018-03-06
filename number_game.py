import random

# Limit the number of guesses
# catch when someone submits a non-integer
# Print "too low" or "too high" messages for bad gusses
# Let people play again

def game():
    # generate a random number between 1 and 10
    secrete_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
            # get a number guess from the player
        try:
            guess = int(input("Guess a number from 1 and 10: "))
            # catch when someone submits a non-integer
        except ValueError:
            print("{} isn't a number!".format(guess))
        else:
            # compare guess to secret number
            if guess == secrete_num:
                print("You got it!!! My number was {}".format(secrete_num))
                break
            elif guess < secrete_num:
                print("My number is higher than {}".format(guess))
            else:
                print("My number is lower than {}".format(guess))
            guesses.append(guess)
        # print hot/miss
    else:
        print("Too bad, you didn't get it.  My number was {}".format(secrete_num))
    play_again = input("Would you like to play again? Y/n ")
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye!")

game()