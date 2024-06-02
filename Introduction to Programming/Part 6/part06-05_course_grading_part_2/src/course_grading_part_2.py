# write your solution here
import math

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


def populate_exam_dict(exams: dict, filename: str):
    """Creates a dictionary of exam points awarded to each student"""
    with open(filename) as file:
        for line in file:
            parts = line.split(";")
            if parts[0] == "id":
                continue
            id = parts[0]
            exam = list(map(int, parts[1:]))
            exams[id] = exam


students = {}
exercises = {}
exams = {}

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"

populate_student_dict(students, student_info)
populate_exercise_dict(exercises, exercise_data)
populate_exam_dict(exams, exam_data)

for id, name in students.items():
    limits = [14, 17, 20, 23, 27]
    if id in exercises:
        exercise_total = sum(exercises[id])
        exercise_points = math.floor(exercise_total / 40 * 10)
    if id in exams:
        exam_points = sum(exams[id])
    total = exam_points + exercise_points
    for i, limit in enumerate(limits):
        if total <= limit:
            grade = i
            break
    else:
        grade = 5
    
    print(f"{name} {grade}")


if __name__ == "__main__":
    pass