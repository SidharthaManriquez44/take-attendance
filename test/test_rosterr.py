from src.attendance.roster import load_student_roster
from src.logger import logger
import pytest


@pytest.fixture
def csv_base(tmp_path):
    # Create a temporary CSV file
    csv_content = "name,age,height,favorite_subject,favorite_animal\nAna,12,150,Math,Cat\n"
    csv_file = tmp_path / "students.csv"
    csv_file.write_text(csv_content, encoding="utf-8")
    return csv_file

# Test 1: Load student to the roster
def test_load_student_roster(csv_base):
    # Call the function using that route
    result = load_student_roster(csv_base)
    assert len(result) == 1
    assert result[0].name == "Ana"

# Test 2: Load an invalid data row skipped
def test_invalid_row_skipped(tmp_path):
    content = "name,age,height,favorite_subject,favorite_animal\nAna,doce,150,Math,Cat\n"
    csv_file = tmp_path / "invalid_students.csv"
    csv_file.write_text(content, encoding="utf-8")
    result = load_student_roster(csv_file)
    assert len(result) == 0

# Tets 3: Load with missing column
def test_missing_column(tmp_path):
    content = "name,age,favorite_subject,favorite_animal\nKaren,8,Math,Dog\n"
    csv_file = tmp_path / "invalid_colum.csv"
    csv_file.write_text(content, encoding="utf-8")
    result = load_student_roster(csv_file)
    assert len(result) == 0

