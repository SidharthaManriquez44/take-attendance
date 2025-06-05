class Seat:
    def __init__(self, label: str):
        """
        Class fo the creation of seats in the classroom and validates if is occupied or not
        the seat could be empty or None
        :param label: id unique of the seats
        """
        self.label = label
        self._student = None

    @property
    def student(self):
        return self._student

    @student.setter
    def student(self, value):
        self._student = value

    def assign_student(self, student):
        """
        Function for assigning students to their seats
        :param student: list of students to assign them
        :return: List of students with their places occupied
        """
        if self.is_occupied():
            raise ValueError("Seat is already occupied.")
        self.student = student

    def is_occupied(self) -> bool:
        """
        Function that validates whether the seat is occupied or not
        :return: bool (True or False)
        """
        return self.student is not None

    def __repr__(self):
        return f"<Seat {self.label}, occupied: {self.is_occupied()}>"
