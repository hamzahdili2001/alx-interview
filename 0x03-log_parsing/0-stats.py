#!/usr/bin/python3
"""0-states.py"""


import sys


def print_stats(status_count, total_size):
    """function that prints statistics"""
    sorted_codes = sorted(status_count.keys())
    print("Total file size: {:d}".format(total_size))

    for code in sorted_codes:
        if status_count[code] != 0:
            print("{:s}: {:d}".format(code, status_count[code]))


try:
    count = 0
    total_size = 0
    status_counts = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    with sys.stdin as f:
        for line in f:
            count += 1
            parts = line.split()
            try:
                file_size = int(parts[-1])
                total_size += file_size
            except ValueError:
                pass

            try:
                status_code = parts[-2]
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except IndexError:
                pass

            if count % 10 == 0:
                print_stats(status_counts, total_size)
        print_stats(status_counts, total_size)

except KeyboardInterrupt:
    print_stats(status_counts, total_size)
    raise
