from src.attendance.student import Student
from src.attendance.classroom import ClassroomOrganizer
import pytest

@pytest.fixture
def base_students():
    students = [
        Student("Ana", 9, 130, "Math", "Dog"),
        Student("Luis", 8, 120, "Science", "Cat"),
        Student("Eva", 9, 125, "Math", "Rabbit")
    ]
    return students

def test_filter_by_subject(base_students):
    organizer = ClassroomOrganizer(base_students)
    math_students = organizer.get_students_with_subject("Math")

    assert len(math_students) == 2
    assert all(s.favorite_subject == "Math" for s in math_students)
    assert {s.name for s in math_students} == {"Ana", "Eva"}

def test_filter_by_age(base_students):
    organizer = ClassroomOrganizer(base_students)
    age_9_students = organizer.get_students_with_age(9)

    assert len(age_9_students) == 2
    assert {s.name for s in age_9_students} == {"Ana", "Eva"}


def test_alphabetical_order(base_students):
    organizer = ClassroomOrganizer(base_students)
    names_in_order = [s.name for s in organizer]

    assert names_in_order == ["Ana", "Eva", "Luis"]

def test_filter_subject_not_found(base_students):
    organizer = ClassroomOrganizer(base_students)
    result = organizer.get_students_with_subject("Art")

    assert result == []

