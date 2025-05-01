# 🎒 Take Attendance

A simple tool to help elementary school teachers organize their student lists, take attendance quickly, and assign classroom seating or teams — all in a fun and efficient way!

This project is developed in **Python** and allows the teacher to upload a CSV file and generate student assignments automatically.

---

## 📌 Features

- ✅ Automatic alphabetical ordering of students.
- ✅ Filter students by favorite subject.
- ✅ Pair or assign students to tables randomly (no repetition).
- ✅ Group students by common interests (e.g. favorite subject).
- ✅ CSV import for custom student lists.
- ✅ Exportable as a standalone executable (`.exe`) for easy use without Python.


---

## 📁 Project Structure

take-attendance/ ├── src/ │ └── attendance/ │ ├── init.py │ ├── classroom_organizer.py # Core logic │ └── roster.py # Student data handling ├── tests/ │ ├── init.py │ └── test_attendance.py # Unit tests ├── dist/ │ └── TakeAttendance.exe # Executable file ├── main.py # Entry point (GUI) ├── requirements.txt ├── README.md ├── .gitignore ├── LICENSE └── data/ └── students.csv 

# Sample input file

## 🚀 Getting Started

1. Download the `.exe` file from [TakeAttendance.exe](dist/TakeAttendance.exe).
2. Run the executable — no need to install Python.
3. Upload your custom student list as a CSV file.

**CSV format required:**

```csv
name,age,height,favorite_subject,favorite_animal
Ana,8,50,Math,Dog
Luis,7,49,Art,Cat
```

## 🧪 Project execution
All you have to do is upload a `CSV` file with the list of students. The required fields are as follows:

- name
- age
- height
- favorite_subject
- favorite_animal

And download the .exe found in the following link [TakeAttendance](dist/TakeAttendance.exe)

`Note`: See example [students.csv](data/students.csv)

## 🧪 Testing
You can run unit tests using:


## 📄 License

This project is licensed under the terms of the [Licencia MIT](LICENSE).


## ✍️ Author
Developed by `Sidhartha Manriquez`.