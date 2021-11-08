"""
Rock paper scissors module
This module contains an implementation of the popular rock paper scissors game
in Python.
"""
from random import choice

GAME_TALLY = {"player_score": 0, "computer_score": 0, "ties": 0}

GAME_CHOICES = ["rock", "paper", "scissors"]

GAME_RULES = {
    "rock": "scissors",  # blunts
    "paper": "rock",  # wraps
    "scissors": "paper",  # cuts
}


def print_game_rules():
    """
    This function prints out the game rules for the user.
    """
    print(
        "The winner is determined by the following schema:\n paper beats "
        "(wraps) rock\n"
        "rock beats (blunts) scissors\n scissors beats (cuts) paper."
    )


def get_number_of_rounds() -> int:
    """
    This function prompts the user to input the number of rounds they would
    like to play the game.
    :returns: number of rounds entered by the user
    :rtype: int
    """
    while True:
        try:
            number_of_rounds = int(
                input(
                    "Welcome to the Rock-Paper-Scissors game.\n"
                    " Please enter the number of rounds you would like to "
                    "play: "
                )
            )
            if number_of_rounds > 0:
                break
            else:
                print(
                    "Invalid input! Please enter a number that is greater"
                    " than 0\n"
                )
        except ValueError:
            print("Invalid input! Please enter a valid number\n")
    return number_of_rounds


def print_final_game_results(
    player_score: int, computer_score: int, ties: int
):
    """
    This function prints the final game results tally
    """
    print(
        f"\n---------------FINAL RESULTS TALLY----------------------\n"
        f"YOU  | Computer     |   Ties\n"
        f"{player_score}    | {computer_score}            | {ties}"
    )


def get_player_choice() -> str:
    """
     Prompts the player to make a choice between rock, paper and scissors and
    returns the player's choice
    :return: player's choice
    :rtype: str
    """
    while True:
        player_game_choice = str(
            input("Please enter a choice between rock, paper and scissors: ")
        ).lower()
        if player_game_choice in GAME_CHOICES:
            break
        else:
            print(
                "Invalid input! Please check if you actually entered either "
                "rock, paper or scissors and try again\n"
            )
    return player_game_choice


def get_computer_choice() -> str:
    """
     Returns a random pick from the list of choices i.e., from rock, paper and
     scissors
    :return: the randomly selected choice
    :rtype: str
    """
    return choice(GAME_CHOICES)


def determine_round_winner(player_game_choice: str, computer_game_choice: str):
    """
    Determines the winner of the current round by comparing the choices made
    by the player and the computer to the rules of the game to see who won.
    The game tally is also updated in this function.
    """
    if player_game_choice == computer_game_choice:
        print(f"Computer choice: {computer_game_choice}")
        print("It's a tie!")
        GAME_TALLY["ties"] = GAME_TALLY["ties"] + 1
    elif GAME_RULES[player_game_choice] == computer_game_choice:
        print(f"Computer choice: {computer_game_choice}")
        print("You win!")
        GAME_TALLY["player_score"] = GAME_TALLY["player_score"] + 1
    else:
        print(f"Computer choice: {computer_game_choice}")
        print("Computer wins!")
        GAME_TALLY["computer_score"] = GAME_TALLY["computer_score"] + 1


def play_game():
    """
    Implements the game logic by calling the other functions in this module
    """
    number_of_game_rounds = get_number_of_rounds()
    print_game_rules()
    for _ in range(number_of_game_rounds):
        computer_choice = get_computer_choice()
        player_choice = get_player_choice()
        determine_round_winner(player_choice, computer_choice)
    print_final_game_results(
        GAME_TALLY["player_score"],
        GAME_TALLY["computer_score"],
        GAME_TALLY["ties"],
    )


if __name__ == "__main__":
    play_game()
