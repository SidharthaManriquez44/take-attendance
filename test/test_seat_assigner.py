from src.attendance.seat_assigner import SeatAssigner
from src.utils.number_to_letter import number_to_letter
import pytest

# Test 1: 3x2 = 6 seats are generated correctly
@pytest.fixture
def base_seats():
    assignation_of_seats = SeatAssigner(3, 2)
    assignation_of_seats.reset()
    return assignation_of_seats

def test_generate_seats(base_seats):
    seats = base_seats.generate_seats()
    assert len(seats) == 6

# Test 2: Assign student to a seat
def test_assign_student(base_seats):
    seats = base_seats.generate_seats()
    seats[0].assign_student("Juan")
    assert seats[0].is_occupied()
    assert seats[0].student == "Juan"

# Test 3: Reassigning to the same seat throws an error
def test_assign_student_same_seat(base_seats):
    seats = base_seats.generate_seats()
    try:
        seats[0].assign_student("Ana")
    except ValueError as e:
        assert str(e) == "Seat is already occupied."

# Test 4: validation function number to letters
def test_number_to_letter():
    assert number_to_letter(3) == ['A', 'B', 'C']
