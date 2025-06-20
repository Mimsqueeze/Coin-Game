from coin_game import play_coin_game

# play the coin game
def main():
    balance = 10
    print(f"Starting balance: {balance}\n")

    while True:
        balance += play_coin_game()
        print(f"Current balance: {balance}")
        
        while (continue_game := input("Do you want to play another game? (y/n)")) not in ["y", "n"]:
            print("Invalid input. Please enter 'y' or 'n'.\n")

        if continue_game == "n":
            break

if __name__ == "__main__":
    main()