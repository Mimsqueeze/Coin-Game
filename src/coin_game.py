# coin_game.py
# simulates a coin game where the player is given a biased or bias coin
# the player can choose to flip the coin or not, cost of flipping is COST
# after each flip, the player can choose to stop flipping the coin, and
# make a decision based on the number of heads flipped
# if the player guesses correctly, they win a reward of REWARD
# otherwise they lose the cost of flipping the coin

import random
from game_parameters import PRIOR, P, REWARD, PENALTY, COST

def play_coin_game(decision_function = None):

    # probability of a biased coin is 0.5
    biased = random.random() < PRIOR

    # track the state of the game
    balance = 0
    heads_flipped = 0
    total_flips = 0

    while True:
        # deduct from balance
        balance -= COST

        # Coin landing
        heads = False

        # Simulate flipping the coin
        if biased:
            heads = random.random() < P
        else:
            heads = random.random() < 0.5
        
        total_flips += 1
        if heads:
            heads_flipped += 1
            print(f"The coin landed HEADS! {heads_flipped} H / {total_flips - heads_flipped} T\n")
        else:
            print(f"The coin landed TAILS! {heads_flipped} H / {total_flips - heads_flipped} T\n")
        

        # Ask the player if they want to continue
        if decision_function:
            continue_flipping, _ = decision_function(heads_flipped, total_flips)
        else:
            while (continue_flipping := input("Do you want to continue flipping? (y/n)")) not in ["y", "n"]:
                print("Invalid input. Please enter 'y' or 'n'.\n")
        continue_flipping = continue_flipping == "y"

        if not continue_flipping:
            break

    # Ask the player to guess whether or not the coin is biased
    if decision_function:
        _, guess = decision_function(heads_flipped, total_flips)
    else:
        while (guess := input("Is the coin biased or unbiased? (biased/unbiased)")) not in ["biased", "unbiased"]:
            print("Invalid input. Please enter 'biased' or 'unbiased'.\n")
    
    if (guess == "biased" and biased):
        balance += REWARD
        print(f"You guessed correctly: the coin was biased! Your net reward is {balance}.\n")
    elif (guess == "unbiased" and not biased):
        balance += REWARD
        print(f"You guessed correctly: the coin was unbiased! Your net reward is {balance}.\n")
    elif (guess == "biased" and not biased):
        balance -= PENALTY
        print(f"You guessed incorrectly: the coin was unbiased. Your net reward is {balance}.\n")
    else:
        balance -= PENALTY
        print(f"You guessed incorrectly: the coin was biased. Your net reward is {balance}.\n")
    
    return balance