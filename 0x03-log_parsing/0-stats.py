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
        if a status code doesn’t appear or is not an integer,
        don’t print anything for this status code
        format: <status code>: <number>
        status codes should be printed in ascending order

"""
from functools import partial
import signal
import sys
import os
import re

pattern = (
    r"(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - "
    r"\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] "
    r'"(GET \/projects\/260 HTTP\/1\.1)" '
    r"(?P<status>\d{3}) "
    r"(?P<size>\d+)"
)
recursion = 0


def handler(signum, frame, report):
    print(report)


totalFileSize = 0
statusDict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
occured = {}
report = {}
try:
    for line in sys.stdin:
        recursion += 1
        match = re.match(pattern, line.rstrip())
        if match:
            totalFileSize += int(match.group("size"))
            status = int(match.group("status"))
            statusDict[status] = statusDict.get(status) + 1
            occured[status] = statusDict.get(status)
            report = f"File size: {totalFileSize}\n"
            for key, value in dict(sorted(occured.items())).items():
                stat = f"{key}: {value}\n"
                report = report + stat
            if recursion == 10:
                recursion = 0
                print(report)
        sign_hand = partial(handler, report=report)
        signal.signal(signal.SIGINT, sign_hand)

except KeyboardInterrupt:
    print(report)
