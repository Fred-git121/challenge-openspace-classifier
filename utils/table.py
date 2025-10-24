class Seat:
    def __init__(self):
        self.is_free = True
        self.occupant = None

    def set_occupant(self, name):
        if self.is_free:
            self.occupant = name
            self.is_free = False
        else:
            print("Seat is already taken.")

    def remove_occupant(self) -> str:
        if not self.is_free:
            print(f"Removing occupant {self.occupant} from seat.")
            last_occupant = self.occupant
            self.is_free = True
            self.occupant = None
            return last_occupant
        else:
            return "The seat is already free."

    def __str__(self):
        if self.occupant is None:
            return "The seat is empty."
        else:
            return f"Occupant of the seat : {self.occupant}."


import itertools

class Table:
    _ids = itertools.count(1)

    def __init__(self, capacity: int) -> None:
        self.number = next(Table._ids)
        self.capacity = capacity
        self.seats = [Seat() for _ in range(self.capacity)]

    def has_free_spot(self) -> bool:
        return any(seat.is_free for seat in self.seats)

    def assign_seat(self, name: str) -> bool:
        for seat in self.seats:
            if seat.is_free:
                seat.set_occupant(name)
                print(f"{name} has been seated at Table {self.number}")
                return True
        return False

    def left_capacity(self) -> int:
        count = 0
        for seat in self.seats:
            if seat.is_free:
                count += 1
        return count


    def __str__(self):
        return f"Table {self.number} (Capacity : {self.capacity} | Free spots : {self.left_capacity()})"
