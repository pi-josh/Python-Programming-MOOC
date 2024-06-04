import csv

def final_points() -> dict:
    start_times = {}
    with open("start_times.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            name, time = line
            hour, minute = map(int, time.split(":"))
            start_minutes = hour * 60 + minute
            start_times[name] = start_minutes
    
    
    submissions = {}
    with open("submissions.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            name, task, points, time = line
            hour, minute = map(int, time.split(":"))
            submissions_minutes = hour * 60 + minute
            points = int(points)
            if name not in submissions:
                submissions[name] = {}
            if task not in submissions[name]:
                submissions[name][task] = {"points": 0, "minutes": 0}
            if points > submissions[name][task]["points"] and submissions_minutes - start_times[name] <= 180:
                submissions[name][task] = {
                    "points": points,
                    "minutes": submissions_minutes
                }
    
    
    final_exam_points = {}
    for name, start_minutes in start_times.items():
        if name in submissions:
            total_points = 0
            for task, data in submissions[name].items():
                total_points += data["points"]
            final_exam_points[name] = total_points

    return final_exam_points


if __name__ == "__main__":
    final_points()
