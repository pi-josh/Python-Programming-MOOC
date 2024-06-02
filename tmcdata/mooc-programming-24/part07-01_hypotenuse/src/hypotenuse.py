# Write your solution here
from math import sqrt, pow

def hypotenuse(leg1: float, leg2: float) -> float:
    return sqrt(pow(leg1,2) + pow(leg2,2))


if __name__ == "__main__":
    print(hypotenuse(3,4))
    print(hypotenuse(5,12))
    print(hypotenuse(1,1))