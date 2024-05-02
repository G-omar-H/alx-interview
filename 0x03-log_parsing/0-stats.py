#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.
1" <status code> <file size>
(if the format is not this one, the line must be skipped)
 After every 10 lines and/or a keyboard interruption (CTRL + C),
 print these statistics from the beginning:
    Total file size: File size: <total size>
        where <total size> is the sum of all
        previous <file size> (see input format above)
    Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        if a status code doesn't appear or is not an integer,
        don't print anything for this status code
        format: <status code>: <number>
        status codes should be printed in ascending order

"""
import signal
import sys
import os
import re

# Regular expression pattern to match the input format
pattern = (
    r"(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - "
    r"\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] "
    r'"GET /projects/260 HTTP/1\.1" '
    r"(?P<status>\d{3}) "
    r"(?P<size>\d+)"
)

total_file_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_statistics():
    """Prints the statistics based on the current data."""
    print(f"File size: {total_file_size}")
    for status_code, count in sorted(status_count.items()):
        if count > 0:
            print(f"{status_code}: {count}")


def signal_handler(sig, frame):
    """Signal handler function to print statistics on interruption."""
    print_statistics()
    sys.exit(0)


# Register signal handler for interruption (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

# Process input line by line
for line in sys.stdin:
    match = re.match(pattern, line.rstrip())
    if match:
        line_count += 1
        total_file_size += int(match.group("size"))
        status_code = int(match.group("status"))
        status_count[status_code] += 1
        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_statistics()
