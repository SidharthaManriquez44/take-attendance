from src.utils.number_to_letter import number_to_letter
from src.attendance.seat import Seat

class SeatAssigner:
    def __init__(self, num_rows: int, seats_per_row: int):
        """
        Seats generating class giving the freedom to choose the quantity depending on the classroom
        :param num_rows: The number of rows of seats in teh classroom
        :param seats_per_row: How many rows have the classroom
        """

        if not (1 <= num_rows <= 26):
            raise ValueError("Number of rows must be between 1 and 26.")

        self.num_rows = num_rows
        self.seats_per_row = seats_per_row
        self.seats: list[Seat] = []

    def generate_seats(self)-> list[Seat]:
        """
        Generating function of the seats
        :return: The list of seat per row
        """
        self.reset()
        self.seats = [
            Seat(f"{row_label}{number}")
            for row_label in number_to_letter(self.num_rows)
            for number in range(1, self.seats_per_row + 1)
        ]
        return self.seats

    def fill_seats(self):
        self.seats = self.generate_seats()

    def reset(self):
        self.seats = []