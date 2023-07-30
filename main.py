import time

from config import directory_watch as dw
from utils.file_management import Directory


def check_calendar():
    pass


def clean_directories():
    for directory in dw:
        Directory(directory)


def record_screentime():
    pass


def main():
    print(f"Checking calendar")
    check_calendar()
    print(f"Cleaning directories")
    clean_directories()
    print(f"Recording screentime")
    record_screentime()
    

if __name__ == "__main__":
    #while True:
    main()
