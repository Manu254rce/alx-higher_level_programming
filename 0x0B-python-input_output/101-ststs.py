#!/usr/bin/python3
"""
This is a Python3 script
"""


import sys
import signal

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats(signal=None, frame=None):
    """
    Function that prints ststistics from computed stdin
    """
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
    if signal is not None:
        sys.exit(0)


signal.signal(signal.SIGINT, print_stats)

for line in sys.stdin:
    try:
        parts = line.split(" ")
        size = int(parts[-1])
        code = int(parts[-5])
        total_size += size
        if code in status_codes:
            status_codes[code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
    except ValueError:
        continue

print_stats()
