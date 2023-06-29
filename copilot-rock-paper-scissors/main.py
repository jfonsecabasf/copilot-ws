# Write a rock, paper, scissors game
# 1. Ask the user to input either rock, paper, scissors, Lizard, or Spock
# 2. Have the computer randomly pick one of the three options
# 3. Compare the user's input to the computer's choice
# 4. Determine who wins
# 5. Print the results
# import random module

import random


def determine_winner(user_choice, computer_choice):
    # create a dictionary of winning combinations
    winning_combinations = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["paper", "spock"],
        "spock": ["rock", "scissors"]
    }

    # determine the winner based on the winning combinations
    if user_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice in winning_combinations[user_choice]:
        return "You win!"
    else:
        return "The computer wins!"


def play_game():
    # create a list of options
    options = ["rock", "paper", "scissors", "lizard", "spock"]

    # create a variable to store the user's choice
    user_choice = input("Enter rock, paper, scissors, lizard, spock: ")

    # create a variable to store the computer's choice
    computer_choice = random.choice(options)

    # print the user's choice
    print("You chose " + user_choice)

    # print the computer's choice
    print("The computer chose " + computer_choice)

    # determine the winner
    result = determine_winner(user_choice, computer_choice)

    # print the results
    print(result)
    print("Thanks for playing!")


if __name__ == '__main__':
    play_game()
