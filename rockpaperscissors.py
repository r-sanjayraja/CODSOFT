import random

def get_user_choice():
    user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome To The Game Of Rock-Paper-Scissors!")
    print("Instructions: Choose Rock, Paper, or Scissors:")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thank you for playing!")

if __name__ == "__main__":
    play_game()
