# Code by cxzlw

import random
import colors
from enum import Enum

title = "Rock Paper Scissors"
description = "The popular game Rock Paper Scissors around the world."


class Decision(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"


class Result(Enum):
    WIN = "win"
    DRAW = "draw"
    LOSE = "lose"


def ask_for_decision():
    while True:
        try:
            player_decision_str = input(
                f"{colors.CYAN}Please enter your decision (rock/paper/scissors): {colors.RESTORE}")
            player_decision = Decision(player_decision_str)
            return player_decision
        except ValueError:
            print(f"{colors.RED}Illegal decision, please re-enter. {colors.RESTORE}")


def get_result(self_decision, opponent_decision) -> Result:
    if opponent_decision == self_decision:
        return Result.DRAW
    match self_decision:
        case Decision.ROCK:
            if opponent_decision == Decision.SCISSORS:
                return Result.WIN
            else:
                return Result.LOSE
        case Decision.PAPER:
            if opponent_decision == Decision.ROCK:
                return Result.WIN
            else:
                return Result.LOSE
        case Decision.SCISSORS:
            if opponent_decision == Decision.PAPER:
                return Result.WIN
            else:
                return Result.LOSE


def game_round() -> Result:
    bot_decision: Decision = random.choice(list(Decision))
    player_decision = ask_for_decision()
    result = get_result(player_decision, bot_decision)

    match result:
        case Result.WIN:
            print(
                f"Bot chose {bot_decision.value}. This round, you {colors.GREEN}WIN{colors.RESTORE}!!")
        case Result.DRAW:
            print(
                f"Bot chose {bot_decision.value}. This round, you {colors.YELLOW}DRAW{colors.RESTORE}!!")
        case Result.LOSE:
            print(f"Bot chose {bot_decision.value}. This round, you {colors.RED}LOSE{colors.RESTORE}!!")

    return result


def main():
    banner_str = ("    ____           --                     --\n    |  |           --        \\   /        --      +"
                  "~~~~~~~~~~~~~~~~+\n---'    |____      --         \\ /         --      |                |\n       (_"
                  "____)     --          X          --      |                |\n      (______)     --         / \\   "
                  "      --      |                |\n      (______)     --    (   )   (   )    --      |              "
                  "  |\n---.__(_____)      --      -       -      --      +~~~~~~~~~~~~~~~~+\n                   --    "
                  "                 --")
    print(
        "".join(random.choice(
            (colors.CYAN, colors.DARK_CYAN, colors.RED, colors.GREEN, colors.DARK_GREEN, colors.YELLOW,
             colors.RESTORE,)) + x
                for x in banner_str))
    print()
    print(f"{colors.YELLOW}RULES:")
    print("\t1. There will be 3 rounds.")
    print("\t2. Whoever scores 2 points first wins.")
    print("\t3. If 3 rounds are over, whoever scores more points wins.")
    print("\t4. If there is a tie, extra games will be played.")
    print(f"{colors.RESTORE}")

    player_points = 0
    bot_points = 0
    for x in range(3):
        result = game_round()
        if result == Result.WIN:
            player_points += 1
        elif result == Result.LOSE:
            bot_points += 1
        if player_points == 2 or bot_points == 2:
            break

    print()

    if player_points > bot_points:
        print(f"You {colors.GREEN} WIN!!{colors.RESTORE}")
    elif bot_points > player_points:
        print(f"You {colors.RED} LOSE!!{colors.RESTORE}")
    else:
        result = Result.DRAW
        while result == Result.DRAW:
            result = game_round()
        if result == Result.WIN:
            print(f"You {colors.GREEN} WIN!!{colors.RESTORE}")
        else:
            print(f"You {colors.RED} LOSE!!{colors.RESTORE}")


if __name__ == '__main__':
    main()
