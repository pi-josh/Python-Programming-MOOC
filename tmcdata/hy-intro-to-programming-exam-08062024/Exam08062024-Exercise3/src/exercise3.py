# Write your solution to exercise 3 here
from fractions import Fraction

def fraction_calculator(calculation: str):
    # partition the calculation
    parts = calculation.split(" ")
    
    # if length of parts is exactly three
    if len(parts) == 3:
        # check if there is a fraction part
        if r'/' in parts[0] and r'/' in parts[2]:
            num1 = convert_to_fraction(parts[0])
            num2 = convert_to_fraction(parts[2])
        else:
            num1 = int(parts[0])
            num2 = int(parts[2])
    else:
        return str(Fraction(parts[0]))
    
    match parts[1]:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2

def convert_to_fraction(fraction: str):
    numerator, denominator = map(int, fraction.split(r"/"))
    return Fraction(numerator, denominator)


fraction = "1/2"
fraction2 = "15/375"
fraction_object = convert_to_fraction(fraction2)
print(convert_to_fraction(fraction))
print(type(fraction_object))
print(fraction_object)

calculation1 = "1/2 + 3/4"
calculation2 = "1/2 - 1/3"
calculation3 = "-1/2 * 1/4"
to_be_reduced = "15/375"

result_of_addition = fraction_calculator(calculation1)
result_of_subtraction = fraction_calculator(calculation2)
result_of_multiplication = fraction_calculator(calculation3)
reduced = fraction_calculator(to_be_reduced)

print(type(to_be_reduced))
print(type(reduced))

print(f'the sum of {calculation1} is', result_of_addition)
print(f'the difference of {calculation2} is', result_of_subtraction)
print(f'the product of {calculation3} is', result_of_multiplication)
print(f'fraction {to_be_reduced} in reduced form is', reduced)

# We'll calculate (1/2 + 3/4) * (1/2 - 1/3) using the results of the previous calculations
calculation4 = f"{result_of_addition} * {result_of_subtraction}"
print(fraction_calculator(calculation4))
