import csv
from typing import List

def read_names_from_csv(input_filepath: str) -> List[str]:
    # Reads a CSV file and returns a list of names.
    names: List[str] = []

    with open(input_filepath, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            names.append(row[0])