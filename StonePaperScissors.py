import random

def get_player_choice():
    player_choice = input("Enter your move (stone, paper, or scissors): ").lower()
    while player_choice not in ["stone", "paper", "scissors"]:
        print("Invalid choice. Please choose from stone, paper, or scissors.")
        player_choice = input("Enter your move (stone, paper, or scissors): ").lower()
    return player_choice

def determine_game_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "stone" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "stone") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_rps_game():
    while True:
        player_move = get_player_choice()
        possible_moves = ["stone", "paper", "scissors"]
        computer_move = random.choice(possible_moves)

        print(f"\nYou chose {player_move}, and the computer chose {computer_move}.\n")

        result = determine_game_winner(player_move, computer_move)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    print("Welcome to the Stone, Paper, Scissors game!")
    play_rps_game()

