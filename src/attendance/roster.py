import csv
from src.attendance.student import Student
from src.logger import logger

def load_student_roster(csv_path):
    student_roster = []
    try:
        with open(csv_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    student = Student(
                        name=row["name"],
                        age=int(row["age"]),
                        height=int(row["height"]),
                        favorite_subject=row["favorite_subject"],
                        favorite_animal=row["favorite_animal"]
                    )
                    student_roster.append(student)
                except (ValueError, KeyError) as ve:
                    logger.warning("The value that you entered is not supported, skipping row")
                    continue
        return student_roster
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {csv_path}")