from src.utils.filter_logic import sort_students_by_name, filter_by_subject, filter_by_age

class ClassroomOrganizer:
    def __init__(self, student_roster):
        self.student_roster = student_roster
        self.sorted_students = sort_students_by_name(student_roster)

    def get_students_with_subject(self, subject):
        return filter_by_subject(self.student_roster, subject)

    def get_students_with_age(self, age):
        return filter_by_age(self.student_roster, age)

    def __iter__(self):
        return iter(self.sorted_students)