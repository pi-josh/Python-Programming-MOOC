# Write your solution here
import urllib.request
import json

def retrieve_all() -> list:
    request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = request.read()
    courses = json.loads(data)
    
    active_courses = []
    for course in courses:
        if course["enabled"] == True:
            full_name = course["fullName"]
            name = course["name"]
            year = course["year"]
            exercises = sum(course["exercises"])
            active_courses.append((full_name, name, year, exercises))
    return active_courses


def retrieve_course(course_name: str) -> dict:
    # retrieve specific course info
    request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = request.read()
    course_info = json.loads(data)
    
    # data to store
    course_statistics = {}
    weeks = 0
    maximum_students = 0
    hours = 0
    hours_average = 0
    exercises = 0
    exercises_average = 0
    
    # calculate values for each data
    for week in course_info:
        weeks += 1
        current_students = course_info[week]["students"]
        if current_students > maximum_students:
            maximum_students = current_students
        hours += course_info[week]["hour_total"]
        exercises += course_info[week]["exercise_total"]
    hours_average = hours // maximum_students
    exercises_average = exercises // maximum_students
    
    # store data in the dictionary
    course_statistics["weeks"] = weeks
    course_statistics["students"] = maximum_students
    course_statistics["hours"] = hours
    course_statistics["hours_average"] = hours_average
    course_statistics["exercises"] = exercises
    course_statistics["exercises_average"] = exercises_average
    
    return course_statistics