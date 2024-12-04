'''
# Name :: Shaaz Nathani
# EID :: ssn774
$ Class :: CS 313 E

# Title :: Speeding Scanner
'''


import time
from typing import Dict, List, Tuple

class TrafficScanDatabase:
    def __init__(self):
        self.scans: Dict[str, List[Dict[str, int]]] = {}
        self.speed_index: Dict[int, List[Tuple[str, Dict[str, int]]]] = {}
        self.time_index: Dict[int, List[Tuple[str, Dict[str, int]]]] = {}

    def insert_scan(self, license_plate: str, speed: int, unix_time: int = None):
        if unix_time is None:
            unix_time = int(time.time())

        scan_record = {
            'speed': speed,
            'unix_time': unix_time
        }

        if license_plate not in self.scans:
            self.scans[license_plate] = []
        self.scans[license_plate].append(scan_record)

        if speed not in self.speed_index:
            self.speed_index[speed] = []
        self.speed_index[speed].append((license_plate, scan_record))

        if unix_time not in self.time_index:
            self.time_index[unix_time] = []
        self.time_index[unix_time].append((license_plate, scan_record))

    def import_from_file(self, filename: str):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) == 3:
                        license_plate = parts[0]
                        speed = int(parts[1])
                        unix_time = int(parts[2])
                        self.insert_scan(license_plate, speed, unix_time)
                print(f"Successfully imported scans from {filename}")
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
        except ValueError:
            print("Error: Invalid file format. Expected 'Plate speed timestamp'.")

    def search_by_speed(self, limit: int) -> List[Tuple[str, Dict[str, int]]]:
        return [
            (plate, record) 
            for speed, records in self.speed_index.items() 
            if speed > limit 
            for plate, record in records
        ]

    def search_by_license_plate(self, license_plate: str) -> List[Dict[str, int]]:
        return self.scans.get(license_plate, [])

    def search_by_time_range(self, start_time: int, end_time: int) -> List[Tuple[str, Dict[str, int]]]:
        return [
            (plate, record) 
            for timestamp, records in self.time_index.items() 
            if start_time <= timestamp <= end_time 
            for plate, record in records
        ]

    def list_all_data(self) -> List[Tuple[str, Dict[str, int]]]:
        all_records = []
        for license_plate, records in self.scans.items():
            for record in records:
                all_records.append((license_plate, record))
        return all_records

def main():
    db = TrafficScanDatabase()

    while True:
        print("\nTraffic Scan Database")
        print("1. Add new scan record")
        print("2. Import scans from file")
        print("3. Search by speed limit")
        print("4. Search by license plate")
        print("5. Search by time range")
        print("6. List all stored data")
        print("7. Exit")

        try:
            choice = int(input("Choose an option (1-7): "))

            if choice == 1:
                # Add new scan record
                license_plate = input("Enter license plate: ")
                speed = int(input("Enter speed: "))
                db.insert_scan(license_plate, speed)
                print("Scan record added successfully.")

            elif choice == 2:
                # Import from file
                filename = input("Enter filename to import: ")
                db.import_from_file(filename)

            elif choice == 3:
                # Search by speed limit
                limit = int(input("Enter speed limit: "))
                results = db.search_by_speed(limit)

                if results:
                    print("\nVehicles exceeding speed limit:")
                    for plate, record in results:
                        print(f"License Plate: {plate}, Speed: {record['speed']}, Timestamp: {record['unix_time']}")
                else:
                    print("No vehicles exceeded the speed limit.")

            elif choice == 4:
                # Search by license plate
                license_plate = input("Enter license plate to search for: ")
                results = db.search_by_license_plate(license_plate)

                if results:
                    print(f"\nScan records for {license_plate}:")
                    for record in results:
                        print(f"Speed: {record['speed']}, Timestamp: {record['unix_time']}")
                else:
                    print("No records found for that license plate.")

            elif choice == 5:
                # Search by time range
                start_time = int(input("Enter start Unix time: "))
                end_time = int(input("Enter end Unix time: "))
                results = db.search_by_time_range(start_time, end_time)

                if results:
                    print("\nScan records within time range:")
                    for plate, record in results:
                        print(f"License Plate: {plate}, Speed: {record['speed']}, Timestamp: {record['unix_time']}")
                else:
                    print("No records found within that time range.")

            elif choice == 6:
                # List all stored data
                results = db.list_all_data()

                if results:
                    print("\nAll Stored Scan Records:")
                    for plate, record in results:
                        print(f"License Plate: {plate}, Speed: {record['speed']}, Timestamp: {record['unix_time']}")
                else:
                    print("No records stored in the database.")

            elif choice == 7:
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please choose a valid option.")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == '__main__':
    main()