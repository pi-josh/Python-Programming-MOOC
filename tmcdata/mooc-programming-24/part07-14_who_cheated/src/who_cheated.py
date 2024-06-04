import csv

def cheaters() -> list:
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
            submission_minutes = hour * 60 + minute
            if name not in submissions:
                submissions[name] = []
            submissions[name].append(submission_minutes)
    
    cheaters = []
    for name in start_times:
        if name in submissions:
            start = start_times[name]
            for submission in submissions[name]:
                if submission - start > 180:
                    cheaters.append(name)
                    break  # No need to check further tasks for this participant
    
    return cheaters

if __name__ == "__main__":
    print(cheaters())
