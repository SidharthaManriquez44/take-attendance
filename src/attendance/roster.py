import csv
from src.attendance.student import Student

def load_student_roster(csv_path):
    student_roster = []

    with open(csv_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student = Student(
                name=row["name"],
                age=int(row["age"]),
                height=int(row["height"]),
                favorite_subject=row["favorite_subject"],
                favorite_animal=row["favorite_animal"]
            )
            student_roster.append(student)

    return student_roster