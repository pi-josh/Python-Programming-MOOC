# Write your solution here
from string import ascii_uppercase

def run(program: list) -> list:
    # create a dictionary of variables set to zero
    variables = {}
    for character in ascii_uppercase:
        variables[character] = 0

    # check each line of commands
    result = []
    index = 0
    while index < len(program):
        line = program[index]
        parts = line.split(" ")
        match parts[0]:
            case 'PRINT':
                if parts[1].isdigit():
                    result.append(int(parts[1]))
                else:
                    result.append(variables[parts[1]])
                index += 1
            case 'MOV':
                if parts[2].isdigit():
                    variables[parts[1]] = int(parts[2])
                else:
                    variables[parts[1]] = variables[parts[2]]
                index += 1
            case 'ADD':
                if parts[2].isdigit():
                    variables[parts[1]] += int(parts[2])
                else:
                    variables[parts[1]] += variables[parts[2]]
                index += 1
            case 'SUB':
                if parts[2].isdigit():
                    variables[parts[1]] -= int(parts[2])
                else:
                    variables[parts[1]] -= variables[parts[2]]
                index += 1
            case 'MUL':
                if parts[2].isdigit():
                    variables[parts[1]] *= int(parts[2])
                else:
                    variables[parts[1]] *= variables[parts[2]]
                index += 1
            case 'JUMP':
                location = parts[1] + ":"
                for i, command in enumerate(program):
                    if location in command:
                        index = i
                        break
            case 'IF':
                operand1, operator, operand2 = parts[1], parts[2], parts[3]
                location = parts[5] + ":"
                if not operand1.isdigit():
                    operand1 = variables[operand1]
                else:
                    operand1 = int(operand1)
                if not operand2.isdigit():
                    operand2 = variables[operand2]
                else:
                    operand2 = int(operand2)
                if condition(operand1, operator, operand2):
                    for i, command in enumerate(program):
                        if location in command:
                            index = i
                            break
                else:
                    index += 1
            case 'END':
                return result

    return result


def condition(operand1, operator, operand2) -> bool:
    match operator:
        case '>':
            return True if operand1 > operand2 else False
        case '<':
            return True if operand1 < operand2 else False
        case '==':
            return True if operand1 == operand2 else False
        case '>=':
            return True if operand1 >= operand2 else False
        case '<=':
            return True if operand1 <= operand2 else False
        case '!=':
            return True if operand1 != operand2 else False


if __name__ == "__main__":
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)