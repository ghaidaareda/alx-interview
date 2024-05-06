#!/usr/bin/python3
"""
alx interveiw
"""
import sys
import re

def is_valid_line(line):
    pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$')
    match = pattern.match(line)
    return match is not None

count = 0
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def print_statistics():
    print(f'Total file size: {total_size}')
    for status_code in status_counts:
        if status_counts[status_code] > 0:
            print(f'{status_code}: {status_counts[status_code]}')

def main():
    global count, total_size, status_counts
    try:
        for line in sys.stdin:
            parts = line.split()
            if is_valid_line(line):
                count += 1
                total_size += int(parts[-1])
                status_code = int(parts[-2])
                if status_code in status_counts:
                    status_counts[status_code] += 1

                if count % 10 == 0:
                    print_statistics()

    except KeyboardInterrupt:
        print_statistics()

if __name__ == "__main__":
    main()
