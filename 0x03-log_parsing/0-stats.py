import sys

def print_metrics(metrics):
    print("Total file size:", metrics['total_size'])
    for code in sorted(metrics['status_codes']):
        print(f"{code}: {metrics['status_codes'][code]}")

def process_line(line, metrics):
    parts = line.split()
    if len(parts) != 7:
        return  # Skip lines with incorrect format
    try:
        code = int(parts[4])
        size = int(parts[5])
    except ValueError:
        return  # Skip lines with non-integer status code or file size
    metrics['total_size'] += size
    metrics['status_codes'][code] = metrics['status_codes'].get(code, 0) + 1

def main():
    metrics = {'total_size': 0, 'status_codes': {}}
    try:
        lines_processed = 0
        for line in sys.stdin:
            process_line(line.strip(), metrics)
            lines_processed += 1
            if lines_processed % 10 == 0:
                print_metrics(metrics)
    except KeyboardInterrupt:
        print_metrics(metrics)

if __name__ == "__main__":
    main()
