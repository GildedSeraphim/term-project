# NAME: Shaaz Nathani
#
# EID: ssn774
#
# CLASS: CS 313E
#
# DESCR: A database analyzer with a locking system and password matching
#

import sqlite3
import time

# Function to initialize and create the database and table if not already created
def init_db():
    conn = sqlite3.connect('vehicle_scans.db')
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS scans (
        license_plate TEXT,
        speed INTEGER,
        unix_time INTEGER,
        PRIMARY KEY (license_plate, unix_time)
    )
    ''')

    # Create indexes for faster searches
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_speed ON scans (speed);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_time ON scans (unix_time);")
    
    conn.commit()
    conn.close()

# Function to insert a new scan record into the database
def insert_scan(license_plate, speed, unix_time):
    conn = sqlite3.connect('vehicle_scans.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO scans (license_plate, speed, unix_time) VALUES (?, ?, ?)", 
                   (license_plate, speed, unix_time))
    
    conn.commit()
    conn.close()

# Function to search for vehicles exceeding a given speed limit
def search_by_speed(limit):
    conn = sqlite3.connect('vehicle_scans.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM scans WHERE speed > ?", (limit,))
    results = cursor.fetchall()

    conn.close()
    return results

# Function to search for scans of a specific license plate
def search_by_license_plate(license_plate):
    conn = sqlite3.connect('vehicle_scans.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM scans WHERE license_plate = ?", (license_plate,))
    results = cursor.fetchall()

    conn.close()
    return results

# Function to search for scans within a time range
def search_by_time_range(start_time, end_time):
    conn = sqlite3.connect('vehicle_scans.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM scans WHERE unix_time BETWEEN ? AND ?", (start_time, end_time))
    results = cursor.fetchall()

    conn.close()
    return results

# Main function to drive the program
def main():
    # Initialize the database
    init_db()

    while True:
        print("\nVehicle Scan Database")
        print("1. Add new scan record")
        print("2. Search by speed limit")
        print("3. Search by license plate")
        print("4. Search by time range")
        print("5. Exit")

        try:
            choice = int(input("Choose an option (1-5): "))

            if choice == 1:
                # Add new scan record
                license_plate = input("Enter license plate: ")
                speed = int(input("Enter speed: "))
                unix_time = int(time.time())  # Use current Unix time for the scan
                insert_scan(license_plate, speed, unix_time)
                print("Scan record added successfully.")

            elif choice == 2:
                # Search by speed limit
                limit = int(input("Enter speed limit: "))
                results = search_by_speed(limit)

                if results:
                    print("\nVehicles exceeding speed limit:")
                    for record in results:
                        print(f"License Plate: {record[0]}, Speed: {record[1]}, Timestamp: {record[2]}")
                else:
                    print("No vehicles exceeded the speed limit.")

            elif choice == 3:
                # Search by license plate
                license_plate = input("Enter license plate to search for: ")
                results = search_by_license_plate(license_plate)

                if results:
                    print(f"\nScan records for {license_plate}:")
                    for record in results:
                        print(f"Speed: {record[1]}, Timestamp: {record[2]}")
                else:
                    print("No records found for that license plate.")

            elif choice == 4:
                # Search by time range
                start_time = int(input("Enter start Unix time: "))
                end_time = int(input("Enter end Unix time: "))
                results = search_by_time_range(start_time, end_time)

                if results:
                    print("\nScan records within time range:")
                    for record in results:
                        print(f"License Plate: {record[0]}, Speed: {record[1]}, Timestamp: {record[2]}")
                else:
                    print("No records found within that time range.")

            elif choice == 5:
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please choose a valid option.")

        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the program
if __name__ == '__main__':
    main()
