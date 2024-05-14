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


count = 0
size = 0
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

try:
    with open(0) as f:
        for line in f:
            count += 1
            arr = line.split()
            try:
                size += int(arr[-1])
            except:
                pass
            try:
                status = arr[-2]
                if status in status_counts:
                    status_counts[status] += 1
            except:
                pass
            if count % 10 == 0:
                print_stats(status_counts, size)
        print_stats(status_counts, size)

except KeyboardInterrupt:
    print_stats(status_counts, size)
    raise
