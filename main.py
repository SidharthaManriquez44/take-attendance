import tkinter as tk
from tkinter import filedialog, messagebox
from src.attendance.roster import load_student_roster
from src.attendance.classroom import ClassroomOrganizer
from src.attendance.seat_assigner import SeatAssigner
from src.logger import logger


class AttendanceApp:
    def __init__(self, rooter):
        self.root = rooter
        self.root.title("Take Attendance")
        self.classroom = None

        # Main buttons
        tk.Button(rooter, text="📂 Upload file CSV", command=self.load_csv).pack(pady=5)
        tk.Button(rooter, text="📋 Show sorted list", command=self.show_sorted_names).pack(pady=5)
        tk.Button(rooter, text="🧑‍🤝‍🧑 Assign tables", command=self.assign_tables).pack(pady=5)
        tk.Button(rooter, text="📚 Filter by subject", command=self.filter_by_subject).pack(pady=5)

        # Text area to display results
        self.output = tk.Text(rooter, width=60, height=20)
        self.output.pack(padx=10, pady=10)

    def load_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not path:
            return
        try:
            roster = load_student_roster(path)
            self.classroom = ClassroomOrganizer(roster)
            messagebox.showinfo("Success", "File uploaded successfully.")
            logger.info("CSV file uploaded successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"The file could not be loaded: {e}")

    def show_sorted_names(self):
        if not self.classroom:
            messagebox.showwarning("First upload a CSV file", "Load the list of students first.")
            logger.error("User need to load the list of students")
            return
        self.output.delete(1.0, tk.END)
        for idx, student in enumerate(self.classroom, 1):
            self.output.insert(tk.END, f"{idx}. {student.name}\n")

    def assign_tables(self):
        if not self.classroom:
            messagebox.showwarning("First upload a CSV file", "Load the list of students first.")
            logger.error("User need to load the list of students before assign tables")
            return

        def assign():
            try:
                rows = int(entry_rows.get())
                columns = int(entry_cols.get())
                if rows <= 0 or columns <= 0:
                    raise ValueError

                assigner = SeatAssigner(rows, columns)
                seats = assigner.generate_seats()

                for student, seat in zip(self.classroom, seats):
                    seat.assign_student(student)

                self.output.delete(1.0, tk.END)
                for seat in seats:
                    if seat.student:
                        self.output.insert(tk.END, f"{seat.label}: {seat.student.name}\n")
                    else:
                        self.output.insert(tk.END, f"{seat.label}: [empty]\n")

                win.destroy()

            except ValueError:
                messagebox.showerror("Invalid input", "Please enter valid positive integers for rows and columns.")
                logger.error("Invalid input Ex 1: int not negative numbers")

        win = tk.Toplevel(self.root)
        win.title("Assign tables")

        tk.Label(win, text="Number of rows:").pack(pady=5)
        entry_rows = tk.Entry(win)
        entry_rows.pack(pady=5)

        tk.Label(win, text="Seats per row:").pack(pady=5)
        entry_cols = tk.Entry(win)
        entry_cols.pack(pady=5)

        tk.Button(win, text="Assign", command=assign).pack(pady=10)

    def filter_by_subject(self):
        if not self.classroom:
            messagebox.showwarning("First upload a CSV file", "Load the list of students first.")
            logger.error("User need to load the list of students")
            return

        def search():
            subject = entry.get().strip()
            if not subject:
                messagebox.showwarning("Without subjects", "Introduce subjects")
                return
            students = self.classroom.get_students_with_subject(subject)
            self.output.delete(1.0, tk.END)
            for student in students:
                self.output.insert(tk.END, f"{student[0]} - {student[1]}\n")
            win.destroy()

        win = tk.Toplevel(self.root)
        win.title("Filter by subject")
        tk.Label(win, text="Favorite subject:").pack(pady=5)
        entry = tk.Entry(win)
        entry.pack(pady=5)
        tk.Button(win, text="Search", command=search).pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()
