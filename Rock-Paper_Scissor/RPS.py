import random


def play():
    user = input(
        "What's your choice? 'r' for rock, 'p' for paper and 's' for scissors\n"
    )
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "It's a tie"
    # r > s , s > p, p > r
    if is_win(user, computer):
        return "You Won!"
    return "You lost!"


def is_win(player, opponent):
    # return true is player win
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True


print(play())
