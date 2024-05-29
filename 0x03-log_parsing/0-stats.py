#!/usr/bin/python3
"""
Log parsing (interview task)
"""

import sys

def print_stats(total_size, status_counts):
    print("File size: {}".format(total_size))
    sorted_status = sorted(status_counts.items(), key=lambda x: int(x[0]))
    for code, count in sorted_status:
        print("{}: {}".format(code, count))

def main():
    total_size = 0
    status_counts = {}

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) != 10:
                continue
            status_code = parts[8]
            if status_code.isdigit() and int(status_code) in [200, 301, 400, 401, 403, 404, 405, 500]:
                total_size += int(parts[9])
                status_counts[status_code] = status_counts.get(status_code, 0) + 1
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
