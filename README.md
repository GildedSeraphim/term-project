# Term Project: Speeding Scanner
## Documentation::
### Libraries
- The libraries I used were the python time library in order to store unix time and the dict, list, and tuple from typing. These were imported to store the data in a dictionary while the program is running.
### TrafficScanDatabase Class
- __init__ ::
-   The init function initializes the dictionaries to store the scan, the speed, and the time. Speed and time are stored as int and the scans of the license plates are stored as strings.
- __insert_scan__ ::
-   The insert_scan function takes in the user input for the plate, the speed, and the time. By default the time will automatically generate when you manually input the plate and speed. The function adds the data to the various dictionaries.
- __import_from_file__ ::
-   This function takes in a filename from the user to input into the dictionaries. If the format of the data is incorrect, or the file is not found the try except will return an error. If successful, the function will iterate through the file and add the logs to the dictionary.
- __search_by_speed__ ::
-   This function takes in an integer speed value defined by the user and searches through the database and adds the record if the speed of the record is greater than the input speed. The return of the function is the piped into the tuple to be output to the user in the main function. This is optimal because It avoids adding unnecessary print statements in the class. 
- __search_by_license_plate__ ::
-   The function simply returns whether or not the dictionary scans contains the user input license plate using the builtin .get() function. 
- __search_by_time_range__ ::
-   The function takes in 2 ints, of time ranges in unix time and outputs all reports within these time ranges. It does this through a similar method of for loop iteration and piping the result into a list of dictionaries for output in the main function.
- __list_all_data__ ::
-   This function iterates through the dictionaries and pipes the output into a list for the main function to print out all the data stored within the dictionary. It does this by making a python array and storing all of the records in it before returning it.


