# Write your solution here
from fractions import Fraction

def fractionate(amount: int) -> list:
    return [Fraction(1, amount) for i in range(amount)]


if __name__ == "__main__":
    for p in fractionate(3):
        print(p)
    
    print()
    
    print(fractionate(5))