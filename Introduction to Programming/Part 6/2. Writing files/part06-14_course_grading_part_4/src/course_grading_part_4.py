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


def get_course_information(course: list, filename: str):
    """Creates a list that contains the name of the course and its credit"""
    with open(filename) as file:
        line1 = file.readline().strip().split(": ")
        line2 = file.readline().strip().split(": ")
        course_name = line1[1]
        credit = line2[1]
        course.append(course_name)
        course.append(credit)


students = {}
exercises = {}
exams = {}
course = []

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
    course_info = input("Course information")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"
    course_info = "course1.txt"

populate_student_dict(students, student_info)
populate_exercise_dict(exercises, exercise_data)
populate_exam_dict(exams, exam_data)
get_course_information(course, course_info)

with open("results.txt", "w") as file:
    header = f"{course[0]}, {course[1]} credits\n"
    file.write(header)
    file.write("======================================\n")
    file.write(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}\n")
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
        
        file.write(f"{name:30}{exercise_total:<10}{exercise_points:<10}{exam_points:<10}{total:<10}{grade:<10}\n")


with open("results.csv", "w") as file:
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
        
        record = f"{id};{name};{grade}\n"
        file.write(record)

if __name__ == "__main__":
    pass