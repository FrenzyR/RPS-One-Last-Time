from enum import IntEnum
import random

from src.RPS_dict import GameResult


class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


def assess_game(user_action, computer_action):
    result = None
    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        result = GameResult.Tie

    # You picked Rock
    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors or computer_action == GameAction.Lizard:
            print("You won!")
            result = GameResult.Victory
        elif computer_action == GameAction.Spock or computer_action == GameAction.Paper:
            print("You lost!")
            result = GameResult.Defeat


    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock or computer_action == GameAction.Spock:
            print("You won!")
            result = GameResult.Victory
        elif computer_action == GameAction.Lizard or computer_action == GameAction.Scissors:
            print("You lost!")
            result = GameResult.Defeat

    # You picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Lizard or computer_action == GameAction.Paper:
            print("You won!")
            result = GameResult.Victory
        elif computer_action == GameAction.Rock or computer_action == GameAction.Spock    :
            print("You lost!")
            result = GameResult.Defeat


    # You picked Lizard
    elif user_action == GameAction.Lizard:
        if computer_action == GameAction.Paper or computer_action == GameAction.Spock:
            print("You won!")
            result = GameResult.Victory
        elif computer_action == GameAction.Rock or computer_action == GameAction.Scissors:
            print("You lost!")
            result = GameResult.Defeat


    # You picked Spock
    elif user_action == GameAction.Spock:
        if computer_action == GameAction.Rock or computer_action == GameAction.Scissors:
            print("You won!")
            result = GameResult.Victory
        elif computer_action == GameAction.Paper or computer_action == GameAction.Lizard:
            print("You lost!")
            result = GameResult.Defeat
    return result

def get_computer_action(user_selection):
    counter_action_map = {
        GameAction.Rock: [GameAction.Paper, GameAction.Spock],
        GameAction.Paper: [GameAction.Scissors, GameAction.Lizard],
        GameAction.Scissors: [GameAction.Rock,GameAction.Spock],
        GameAction.Lizard: [GameAction.Rock, GameAction.Scissors],
        GameAction.Spock: [GameAction.Lizard, GameAction.Paper],
    }

    computer_action = GameAction(counter_action_map[user_selection][random.randint(0, 1)])

    print(f"Computer picked {computer_action.name}.")

    return computer_action


def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'


def main():

    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action(user_action)
        assess_game(user_action, computer_action)

        if not play_another_round():
            break


if __name__ == "__main__":
    main()
