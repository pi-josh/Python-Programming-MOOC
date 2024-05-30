# Write your solution here


def filter_solutions():
    filename = "solutions.csv"
    correct = []
    incorrect = []
    
    with open(filename) as file:
        for line in file:
            name, problem, result = line.strip().split(";")
            record = f"{name};{problem};{result}"
            
            if eval(problem) == int(result):
                correct.append(record)
            else:
                incorrect.append(record)
    
    # Store the correct and incorrect records in each
    # respective text files
    with open("correct.csv", "w") as file:
        for record in correct:
            file.write(record+"\n")
    
    with open("incorrect.csv", "w") as file:
        for record in incorrect:
            file.write(record+"\n")


if __name__ == "__main__":
    filter_solutions()