import random

def roll_dice():
    return random.randint(1, 6)

def play_turn(player_name):
    input(f"{player_name}, press Enter to roll the dice...")
    roll = roll_dice()
    print(f"{player_name} rolled a {roll}")
    return roll

def play_game():
    print("🎲 Welcome to the Dice Game!")
    mode = input("Choose mode - (1) Player vs Computer, (2) Player 1 vs Player 2: ")

    if mode == "1":
        player1 = input("Enter your name: ")
        player2 = "Computer"
    elif mode == "2":
        player1 = input("Enter Player 1 name: ")
        player2 = input("Enter Player 2 name: ")
    else:
        print("Invalid mode. Exiting.")
        return

    target_score = 50
    print(f"\n🎯 Target score is set to: {target_score}")

    scores = {player1: 0, player2: 0}
    tries = {player1: 0, player2: 0}

    winner = None

    while True:
        for player in [player1, player2]:
            print(f"\n--- {player}'s Turn ---")
            roll = roll_dice() if player == "Computer" else play_turn(player)
            scores[player] += roll
            tries[player] += 1
            print(f"{player}'s total score: {scores[player]}")

            if scores[player] >= target_score:
                winner = player
                break
        if winner:
            break

    print("\n=== Game Over ===")
    print(f"🏆 {winner} wins the game!")
    print(f"\n🎯 Final Scores and Tries:")
    print(f"{player1} - Score: {scores[player1]}, Tries: {tries[player1]}")
    print(f"{player2} - Score: {scores[player2]}, Tries: {tries[player2]}")

    replay = input("\nDo you want to play again? (y/n): ").lower()
    if replay == 'y':
        play_game()
    else:
        print("Thanks for playing! Goodbye 👋")

# Start the game
if __name__ == "__main__":
    play_game()
