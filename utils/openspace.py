class Openspace:
    def __init__(self, tables: list) -> None:
        self.tables = tables
        self.number_of_tables = len(tables)

    def organize_tables(self) -> list:
        tables = []
        for table in self.tables:
            tables.append(table)
    def display_tables(self) -> list:
        for table in self.tables:
            print(table)
            for i, seat in enumerate(table.seats, start=1):
                status = seat.occupant if not seat.is_free else "Empty"
                print(f"   Seat {i}: {status}")