from string import ascii_uppercase

def run(program: list) -> list:
    # Initialize variables
    variables = {char: 0 for char in ascii_uppercase}
    labels = {}
    result = []
    
    # First pass: identify labels
    for index, line in enumerate(program):
        if line.endswith(":"):
            label = line[:-1]
            labels[label] = index
    
    # Function to evaluate condition
    def condition(op1, operator, op2):
        if operator == '>':
            return op1 > op2
        elif operator == '<':
            return op1 < op2
        elif operator == '==':
            return op1 == op2
        elif operator == '>=':
            return op1 >= op2
        elif operator == '<=':
            return op1 <= op2
        elif operator == '!=':
            return op1 != op2
    
    # Function to get the value from either a variable or an integer
    def get_value(value):
        if value in variables:
            return variables[value]
        return int(value)
    
    # Execute the program
    index = 0
    while index < len(program):
        parts = program[index].split()
        command = parts[0]
        
        if command == "PRINT":
            value = get_value(parts[1])
            result.append(value)
            index += 1
        elif command == "MOV":
            variables[parts[1]] = get_value(parts[2])
            index += 1
        elif command == "ADD":
            variables[parts[1]] += get_value(parts[2])
            index += 1
        elif command == "SUB":
            variables[parts[1]] -= get_value(parts[2])
            index += 1
        elif command == "MUL":
            variables[parts[1]] *= get_value(parts[2])
            index += 1
        elif command == "JUMP":
            index = labels[parts[1]]
        elif command == "IF":
            op1 = get_value(parts[1])
            operator = parts[2]
            op2 = get_value(parts[3])
            if condition(op1, operator, op2):
                index = labels[parts[5]]
            else:
                index += 1
        elif command == "END":
            break
        elif command.endswith(":"):
            index += 1
        else:
            raise ValueError(f"Unknown command: {command}")
    
    return result

if __name__ == "__main__":
    # Test cases
    program1 = [
        "MOV A 1",
        "MOV B 2",
        "PRINT A",
        "PRINT B",
        "ADD A B",
        "PRINT A",
        "END"
    ]
    print(run(program1))  # Output: [1, 2, 3]

    program2 = [
        "MOV A 1",
        "MOV B 10",
        "begin:",
        "IF A >= B JUMP quit",
        "PRINT A",
        "PRINT B",
        "ADD A 1",
        "SUB B 1",
        "JUMP begin",
        "quit:",
        "END"
    ]
    print(run(program2))  # Output: [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]

    program3 = [
        "MOV A 1",
        "MOV B 1",
        "begin:",
        "PRINT A",
        "ADD B 1",
        "MUL A B",
        "IF B <= 10 JUMP begin",
        "END"
    ]
    print(run(program3))  # Output: [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

    program4 = [
        "MOV N 50",
        "PRINT 2",
        "MOV A 3",
        "begin:",
        "MOV B 2",
        "MOV Z 0",
        "test:",
        "MOV C B",
        "new:",
        "IF C == A JUMP error",
        "IF C > A JUMP over",
        "ADD C B",
        "JUMP new",
        "error:",
        "MOV Z 1",
        "JUMP over2",
        "over:",
        "ADD B 1",
        "IF B < A JUMP test",
        "over2:",
        "IF Z == 1 JUMP over3",
        "PRINT A",
        "over3:",
        "ADD A 1",
        "IF A <= N JUMP begin"
    ]
    print(run(program4))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]