# src/attendance/clasroom_organizer.py
def _sort_alphabetically(students):
    return sorted([student['name'] for student in students])


class ClassroomOrganizer:
    def __init__(self, student_roster):
        self.student_roster = student_roster
        self.sorted_names = _sort_alphabetically(student_roster)

    def get_students_with_subject(self, subject):
        return sorted(
            [(student['name'], subject) for student in self.student_roster if student['favorite_subject'] == subject],
            key=lambda x: x[0]
        )

    def __iter__(self):
        return iter(self.sorted_names)

    def get_student_with_age(self, age):
        return [
            (student['name'], age)
            for student in self.student_roster
            if student['age'] == age
        ]
