#!/usr/bin/python3
import sys


def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def parse_line(line, total_size, status_codes):
    try:
        elements = line.split()
        if len(elements) >= 9:
            status_code = int(elements[-2])
            file_size = int(elements[-1])
            total_size += file_size

            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                if status_code not in status_codes:
                    status_codes[status_code] = 1
                else:
                    status_codes[status_code] += 1

        return total_size, status_codes
    except ValueError:
        return total_size, status_codes


def main():
    line_count = 0
    total_size = 0
    status_codes = {}

    try:
        for line in sys.stdin:
            line_count += 1
            total_size, status_codes = parse_line(line,
                                                  total_size, status_codes)

            if line_count == 10:
                print_stats(total_size, status_codes)
                line_count = 0

    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
