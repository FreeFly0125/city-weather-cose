import csv
import os
from typing import List


class LocationDetail:
    data = {}

    def __init__(self) -> None:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        with open(f"{current_directory}/location_info.csv") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                self.data[row[1]] = [row[0], float(row[2]), float(row[3])]


locationDetail = LocationDetail()
