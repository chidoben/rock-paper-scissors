import pytest

from rps.rps import (
    get_number_of_rounds,
    get_player_choice,
    get_computer_choice,
    determine_round_winner,
    GAME_CHOICES,
    GAME_TALLY,
)


def test_get_number_of_rounds_returns_the_right_number_of_rounds(monkeypatch):
    """
    Test that get_number_of_rounds returns the right number of rounds entered
    by the player
    """
    expected_number_of_rounds = 12
    monkeypatch.setattr("builtins.input", lambda _: expected_number_of_rounds)
    returned_number_of_rounds = get_number_of_rounds()
    assert expected_number_of_rounds == returned_number_of_rounds


def test_get_number_of_rounds_returns_number_of_rounds():
    """ """


def test_get_player_choice_returns_player_choice(monkeypatch):
    """
    Test that get_player_choice returns the right game choice entered
    by the player.
    """
    expected_game_choice = "rock"
    monkeypatch.setattr("builtins.input", lambda _: expected_game_choice)
    returned_game_choice = get_player_choice()
    assert expected_game_choice == returned_game_choice


def test_get_computer_choice_returns_valid_game_choice():
    """
    Test that get_computer_choice returns a valid game choice i.e., a game
    choice that is in the list of possible game choices
    """
    computer_choice = get_computer_choice()
    assert computer_choice in GAME_CHOICES


@pytest.mark.parametrize(
    "player_choice,computer_choice,winner_score_argument,loser_score_argument",
    [
        ("rock", "rock", "ties", "computer_score"),
        ("rock", "paper", "computer_score", "player_score"),
    ],
)
def test_determine_round_winner_updates_tally_with_the_right_winner(
    player_choice, computer_choice, winner_score_argument, loser_score_argument
):
    """
    Test that calling determine_round_winner updates the score of the winner of
    the current round and that the score of the loser is not updated
    """
    determine_round_winner(player_choice, computer_choice)
    assert GAME_TALLY[winner_score_argument] == 1
    assert GAME_TALLY[loser_score_argument] == 0
