# Write your solution here
def ask_result() -> list:
    result = []
    while True:
        exam_exercise = input("Exam points and exercises completed: ").split()
        if exam_exercise:
            exam, exercise = map(int, exam_exercise)
            result.append([exam, exercise])
        else:
            return result

def analyze_result(results: list) -> list:
    grades = []
    points = []
    for result in results:
        exam_point = result[0]
        exercise_point = int(result[1] / 100 * 10)
        total_point = exam_point + exercise_point
        points.append(total_point)
        if total_point < 15 or exam_point < 10:
            grades.append(0)
        elif total_point < 18:
            grades.append(1)
        elif total_point < 21:
            grades.append(2)
        elif total_point < 24:
            grades.append(3)
        elif total_point < 28:
            grades.append(4)
        else:
            grades.append(5)
    return grades, points

def print_result(grades: list, points: list):
    points_average = sum(points) / len(points)

    # Getting the percentage of those who passed the course
    pass_counter = 0
    for grade in grades:
        if grade != 0:
            pass_counter += 1
    pass_percentage = pass_counter / len(grades) * 100
    
    print("Statistics: ")
    print(f"Points average: {points_average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        count = grades.count(i)
        print(f"  {i}: " + "*" * count)

def main():
    result_list = ask_result()
    grade_list, point_list = analyze_result(result_list)
    print_result(grade_list, point_list)


main()