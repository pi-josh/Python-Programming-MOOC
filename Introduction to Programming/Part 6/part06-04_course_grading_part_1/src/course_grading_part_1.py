# write your solution here
def populate_student_dict(students: dict, filename: str):
    """Creates a dictionary of student info"""
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(";")
            if parts[0] == "id":
                continue
            id = parts[0]
            name = f"{parts[1]} {parts[2]}"
            students[id] = name


def populate_exercise_dict(exercises: dict, filename: str):
    """Creates a dictionary of exercises completed"""
    with open(filename) as file:
        for line in file:
            parts = line.split(";")
            if parts[0] == "id":
                continue
            id = parts[0]
            exercise = list(map(int, parts[1:]))
            exercises[id] = exercise


students = {}
exercises = {}
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

populate_student_dict(students, student_info)
populate_exercise_dict(exercises, exercise_data)

for id, name in students.items():
    if id in exercises:
        print(f"{name} {sum(exercises[id])}")
    else:
        print(f"{name} no exercises")


if __name__ == "__main__":
    pass