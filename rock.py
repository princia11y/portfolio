import random

# Initialize scores
user_score = 0
computer_score = 0

def display_instructions():
    print("\n--- Welcome to Rock, Paper, Scissors ---")
    print("Instructions:")
    print("Choose 'rock', 'paper', or 'scissors' to play.")
    print("Enter 'q' to quit the game.")
    print("Good luck!\n")

def get_user_choice():
    choice = input("Enter your choice (rock/paper/scissors or q to quit): ").lower()
    while choice not in ['rock', 'paper', 'scissors', 'q']:
        print("Invalid input. Please enter 'rock', 'paper', 'scissors', or 'q'.")
        choice = input("Enter your choice: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_round_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == "draw":
        print("It's a draw!")
    elif winner == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")

def display_scores(user_score, computer_score):
    print("\n--- Current Scores ---")
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}\n")

def play_game():
    global user_score, computer_score
    display_instructions()
    
    while True:
        user_choice = get_user_choice()
        if user_choice == 'q':
            print("Thank you for playing! Final scores:")
            display_scores(user_score, computer_score)
            break
        
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        display_round_result(user_choice, computer_choice, winner)
        display_scores(user_score, computer_score)

# Start the game
play_game()
