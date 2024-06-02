# Write your solution here
from random import choice

def roll(die: str) -> int:
    match die:
        case 'A':
            values = [3, 3, 3, 3, 3, 6]
        case 'B':
            values = [2, 2, 2, 5, 5, 5]
        case 'C':
            values = [1, 4, 4, 4, 4, 4]
    
    return choice(values)


def play(die1: str, die2: str, times: int) -> tuple:
    die1_wins = 0
    die2_wins = 0
    ties = 0
    for i in range(times):
        roll_die1 = roll(die1)
        roll_die2 = roll(die2)
        if roll_die1 > roll_die2:
            die1_wins += 1
        elif roll_die2 > roll_die1:
            die2_wins += 1
        else:
            ties += 1
    
    return die1_wins, die2_wins, ties


if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()
    result = play("A", "C", 1000)
    print(result)
    result = play("A", "B", 100)
    print(result)

