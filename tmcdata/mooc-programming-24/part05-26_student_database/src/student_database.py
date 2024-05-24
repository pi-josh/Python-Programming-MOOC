# Write your solution here
def add_student(students: dict, student_name: str):
    if student_name not in students:
        students[student_name] = []


def print_student(students: dict, student_name: str):
    if student_name in students:
        print(f"{student_name}:")
        if students[student_name]:
            course_count = len(students[student_name])
            average = sum([grade[1] for grade in students[student_name]]) / course_count
            print(f" {course_count} completed courses:")
            for course in students[student_name]:
                print(f"  {course[0]} {course[1]}")
            print(f" average grade {average}")
        else:
            print(" no completed courses")
    else:
        print(f"{student_name}: no such person in the database")


def add_course(students: dict, student_name: str, course: tuple):
    if student_name in students:
        for courses in students[student_name]:
            if course[0] == courses[0]:
                if course[1] > courses[1]:
                    new_courses = list(students[student_name])
                    new_courses[new_courses.index(courses)] = course
                    students[student_name] = new_courses
                break
        else:
            if course[1] != 0:
                students[student_name].append(course)


def summary(students: dict):
    student_count = len(students)
    
    # Get the student with the most courses completed
    most_courses_count = max([len(students[student]) for student in students])
    most_courses_name = ""
    for student in students:
        if len(students[student]) == most_courses_count:
            most_courses_name = student
            break
    
    # Get the student with the best average
    best_average = 0
    best_average_name = ""
    for student in students:
        record = {}
        course_count = len(students[student])
        average = sum([grade[1] for grade in students[student]]) / course_count
        if best_average < average:
            best_average = average
            best_average_name = student    

    # Print the summary
    print(f"students {student_count}")
    print(f"most courses completed {most_courses_count} {most_courses_name}")
    print(f"best average grade {best_average} {best_average_name}")
    

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Software Development Methods", 1))
    add_course(students, "Peter", ("Software Development Methods", 5))
    print_student(students, "Peter")