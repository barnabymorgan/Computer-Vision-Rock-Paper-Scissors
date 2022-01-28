import time
from computer_guess import get_computer_selection
from player_guess import get_player_selection
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


def play_game():
    game_score = [0, 0]

    while True:
        player_action = Action(get_player_selection())
        computer_action = Action(get_computer_selection())
        print(f"\nYou chose {player_action.name}, \
            computer chose {computer_action.name}.\n")

        result = play_result(player_action, computer_action)

        if result == 1:
            i = 0
        elif result == 2:
            i = 1
        else:
            continue

        game_score[i] += 1

        if game_score[0] == 3 or game_score[1] == 3:
            if game_score[0] == 3:
                print("YOU WIN THE MATCH", game_score)
            else:
                print("CPU WIN THE MATCH", game_score)
            break


def play_result(player_action, computer_action):
    victories = {
        Action.Rock: [Action.Scissors],  # Rock beats scissors
        Action.Paper: [Action.Rock],  # Paper beats rock
        Action.Scissors: [Action.Paper]  # Scissors beats paper
    }

    defeats = victories[player_action]
    if player_action == computer_action:
        print(f"Both players selected {player_action.name}. It's a tie!")
        return 0
    elif computer_action in defeats:
        print(f"{player_action.name} beats {computer_action.name}! You win!")
        return 1
    else:
        print(f"{computer_action.name} beats {player_action.name}! You lose.")
        return 2



play_game()
