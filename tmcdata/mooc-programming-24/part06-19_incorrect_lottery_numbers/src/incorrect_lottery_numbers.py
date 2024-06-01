# Write your solution here
def filter_incorrect():
    correct = []
    with open("lottery_numbers.csv") as file:
        for line in file:
            try:
                week, winning_numbers = line.strip().split(";")
                week, w_number = week.split(" ")
                
                # will raise an error if value in winning_numbers is not convertible to int
                winning_numbers = list(map(int, winning_numbers.split(",")))
                is_week_number_incorrect = not w_number.isdigit()
                is_few_numbers = not len(winning_numbers) == 7
                
                is_numbers_not_in_range = False
                has_duplicate = False
                for target in winning_numbers:
                    if not (target >= 1 and target <= 39):
                        is_numbers_not_in_range = True
                        break
                    
                    if not winning_numbers.count(target) == 1:
                        has_duplicate = True
                        break
                
                if is_week_number_incorrect or is_few_numbers or \
                    is_numbers_not_in_range or has_duplicate:
                        raise ValueError(f"{w_number}, {winning_numbers}")
            except:
                continue
            
            record = f"{week} {w_number};{",".join(map(str, winning_numbers))}\n"
            correct.append(record)
            
    with open("correct_numbers.csv", "w") as file:
        for record in correct:
            file.write(record)


if __name__ == "__main__":
    filter_incorrect()