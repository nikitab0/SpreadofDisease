"""Project 1 reading csv file."""
from typing import List, Dict
from csv import DictReader
import sys


__author__ = "730393935"


def main() -> None:
    """Entrypoint of program to run as a module."""
    read_args()
    file_handle = open(sys.argv[1], "r", encoding="utf8")
    csv_reader = DictReader(file_handle)    
    
    if operation_exist(sys.argv[3]) is False:
        print("Invalid operation: " + sys.argv[3])
    if column_exist(csv_reader, sys.argv[2]) is False:
        print("Invalid column: " + sys.argv[2])
    else:
        if str(sys.argv[3]) == "list":
            print(list(sys.argv[1], sys.argv[2]))
        if str(sys.argv[3]) == "min":
            print(min(sys.argv[1], sys.argv[2]))
        if str(sys.argv[3]) == "max":
            print(max(sys.argv[1], sys.argv[2]))
        if str(sys.argv[3]) == "avg":
            print(avg(sys.argv[1], sys.argv[2]))
        if str(sys.argv[3]) == "chart":
            chart_data(list(sys.argv[1], sys.argv[2]), sys.argv[2], date_list(sys.argv[1], sys.argv[2]))
    file_handle.close()
        

def read_args() -> Dict[str, str]:
    """Checks for valid args."""
    if len(sys.argv) != 4:
        print("Usage: python -m projects.pj01.weather [FILE] [COLUMN] [OPERATION]")
        exit()
    return {
        "FILE": sys.argv[1],
        "COLUMN": sys.argv[2],
        "OPERATION": sys.argv[3]
    }


def list(file_path: str, column_name: str) -> List[float]:
    """Produces and prints a list for each of the columns arguments."""
    result: List[float] = []
    file_handle = open(file_path, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)   
    for column in csv_reader:
        try:
            result.append(float(column[column_name]))
        except ValueError:
            ...
    file_handle.close()
    return result


def date_list(file_path: str, column_name: str) -> List[str]:
    """Produces and prints a list for each of the columns arguments."""
    result: List[str] = []
    file_handle = open(file_path, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)   
    for column in csv_reader:
        if column[column_name] != "":
            date_part: str = str(column["DATE"])
            result.append(date_part[0: 10])
    file_handle.close()
    return result


def min(file_path: str, column_name: str) -> float:
    """Returns the minimum value of a column."""
    column_list: List[float] = list(file_path, column_name)
    min_value: float = column_list[0]
    for i in range(0, len(column_list)):
        if column_list[i] < min_value:
            min_value = column_list[i]
    return min_value


def max(file_path: str, column_name: str) -> float:
    """Returns the minimum value of a column."""
    column_list: List[float] = list(file_path, column_name)
    max_value: float = column_list[0]
    for i in range(0, len(column_list)):
        if column_list[i] > max_value:
            max_value = column_list[i]
    return max_value


def avg(file_path: str, column_name: str) -> float:
    """Produces the average value of a column."""
    column_list: List[float] = list(file_path, column_name)
    sum: float = 0.0
    for i in range(0, len(column_list)):
        sum = sum + column_list[i]
    average: float = sum / len(column_list)
    return average


def column_exist(reader: DictReader, column_name: str) -> bool:
    """Determines if a given column exists in the Data."""
    return_column: bool = False
    for column in reader:
        for row in column:
            if row == column_name:
                return_column = True
    return return_column


def operation_exist(operation: str) -> bool:
    """Determines if a given operation exists in the module."""
    all_operations: List[str] = ["avg", "chart", "max", "min", "list"]
    result: bool = False
    if operation in all_operations:
        result = True
    return result


def chart_data(data: List[float], column: str, dates: List[str]) -> None:
    """Charts the data with date on x-axis and data for column name on y-axis."""
    import matplotlib.pyplot as plt
    plt.plot(dates, data)
    plt.xlabel("Date")
    plt.ylabel(column)
    plt.show()

    
if __name__ == "__main__":
    main()