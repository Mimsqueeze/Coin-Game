from coin_game import play_coin_game

# naive decision functions chooses biased if first flip is H, unbiased if first flip is T
def naive_decision(heads_flipped, total_flipped):
    if heads_flipped > 0:
        return("n", "biased")
    else:
        return("n", "unbiased")

# play the coin game
def main():
    balance = 0
    print(f"Starting balance: {balance}\n")

    num_games = 100000
    for i in range(num_games):
        balance += play_coin_game(naive_decision)
    
    print(f"Final balance after {num_games} games: {balance}")
    print(f"Average per game: {balance/num_games:.4f}")

if __name__ == "__main__":
    main()