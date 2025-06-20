from coin_game import play_coin_game

# naive decision functions chooses biased if first flip is H, unbiased if first flip is T
def naive_decision(heads_flipped, total_flipped):
    if heads_flipped > 0:
        return("n", "biased")
    else:
        return("n", "unbiased")

# play the coin game
def main():
    balance = 10
    print(f"Starting balance: {balance}\n")

    for _ in range(10000):
        balance += play_coin_game(naive_decision)
    
    print(f"Ending balance: {balance}\n")

if __name__ == "__main__":
    main()