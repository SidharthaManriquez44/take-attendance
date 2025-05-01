# main.py
import tkinter as tk
from tkinter import filedialog, messagebox
from src.attendance.roster import load_student_roster
from src.attendance.classroom_organizer import ClassroomOrganizer
import itertools


class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Take Attendance")
        self.classroom = None

        # Main buttons
        tk.Button(root, text="📂 Upload file CSV", command=self.load_csv).pack(pady=5)
        tk.Button(root, text="📋 Show sorted list", command=self.show_sorted_names).pack(pady=5)
        tk.Button(root, text="🧑‍🤝‍🧑 Assign tables", command=self.assign_tables).pack(pady=5)
        tk.Button(root, text="📚 Filter by subject", command=self.filter_by_subject).pack(pady=5)

        # Text area to display results
        self.output = tk.Text(root, width=60, height=20)
        self.output.pack(padx=10, pady=10)

    def load_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not path:
            return
        try:
            roster = load_student_roster(path)
            self.classroom = ClassroomOrganizer(roster)
            messagebox.showinfo("Success", "File uploaded successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"The file could not be loaded: {e}")

    def show_sorted_names(self):
        if not self.classroom:
            messagebox.showwarning("First upload a CSV file", "Load the list of students first.")
            return
        self.output.delete(1.0, tk.END)
        for idx, student in enumerate(self.classroom, 1):
            self.output.insert(tk.END, f"{idx}. {student}\n")

    def assign_tables(self):
        if not self.classroom:
            messagebox.showwarning("First upload a CSV file", "Load the list of students first.")
            return
        students = list(self.classroom)
        all_pairs = list(itertools.combinations(students, 2))
        used = set()
        tables = []

        for pair in all_pairs:
            if pair[0] not in used and pair[1] not in used:
                tables.append(pair)
                used.update(pair)
            if len(tables) == len(students) // 2:
                break

        self.output.delete(1.0, tk.END)
        for idx, pair in enumerate(tables, 1):
            self.output.insert(tk.END, f"Table {idx}: {pair[0]} y {pair[1]}\n")

    def filter_by_subject(self):
        if not self.classroom:
            messagebox.showwarning("First upload a CSV file", "Load the list of students first.")
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
