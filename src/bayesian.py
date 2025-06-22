from coin_game import play_coin_game
from game_parameters import PRIOR, P, REWARD, PENALTY, COST, MAX_FLIPS

# use bayesian analysis to determine whether or not to guess or continue the game
# by comparing expected values
def bayesian_decision(h, n):
    # probability of guess being correct
    P_b = compute_biased_probability(h, n)
    P_u = compute_unbiased_probability(h, n)
    P_correct = max(P_b, P_u)

    # expected value of stopping to guess
    E_guess = REWARD * P_correct - PENALTY * (1 - P_correct)
    
    # base case
    if n >= MAX_FLIPS:
        if P_b > P_u:
            return ("n", "biased")
        else:
            return ("n", "unbiased")
    
    # estimate probability of getting heads on next flip
    P_h = P_b * P + P_u * 0.5

    # expected value of continuing the game
    E_continue = -COST + P_h * expected_reward(h+1, n+1) + (1 - P_h) * expected_reward(h, n+1)

    if (E_guess >= E_continue):
        if P_b > P_u:
            return ("n", "biased")
        else:
            return ("n", "unbiased")
    else:
        return ("y", "")


# save results for expected_reward
dp = dict()

# computes the expected reward at the game state
def expected_reward(h, n):
    if (h, n) in dp.keys():
        return dp.get((h, n))

    # probability of guess being correct
    P_b = compute_biased_probability(h, n)
    P_u = compute_unbiased_probability(h, n)
    P_correct = max(P_b, P_u)

    # expected value of stopping to guess
    E_guess = REWARD * P_correct - PENALTY * (1 - P_correct)

    # base case
    if n >= MAX_FLIPS:
        return E_guess
    
    # estimate probability of getting heads on next flip
    P_h = P_b * P + P_u * 0.5

    # expected value of continuing the game
    E_continue = -COST + P_h * expected_reward(h+1, n+1) + (1 - P_h) * expected_reward(h, n+1)

    dp[(h, n)] = max(E_guess, E_continue)

    return max(E_guess, E_continue)

def compute_biased_probability(h, n):
    if n == 0:
        return PRIOR
    
    # P(biased|h,n) = P(h,n|biased)/(P(h,n|biased)+P(h,n|unbiased))
    num = PRIOR*(P**h)*((1-P)**(n-h))
    denom = PRIOR*(P**h)*((1-P)**(n-h)) + (1-PRIOR)*0.5**n
    return num/denom

def compute_unbiased_probability(h, n):
    return 1 - compute_biased_probability(h, n)

# play the coin game
def main():
    balance = 0
    print(f"Starting balance: {balance}\n")

    num_games = 100000
    for i in range(num_games):
        balance += play_coin_game(bayesian_decision)
    
    print(f"Final balance after {num_games} games: {balance}")
    print(f"Average per game: {balance/num_games:.4f}")

if __name__ == "__main__":
    main()