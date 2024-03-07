import random

def play_round():
    choices = ["rock", "paper", "scissors"]

    # User input
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Validate user input
    while user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Computer randomly selects
    computer_choice = random.choice(choices)

    # Display choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")

    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        result = "You win!"
    else:
        result = "You lose!"

    print(result)
    return result

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        result = play_round()

        # Update scores
        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        # Display scores
        print(f"\nScores - You: {user_score}, Computer: {computer_score}")

        # Ask to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
