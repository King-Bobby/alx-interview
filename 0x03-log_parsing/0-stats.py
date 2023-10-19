#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics:
"""


import sys
from collections import defaultdict


# Initialize variables to keep track of metrics
total_file_size = 0
status_code_count = defaultdict(int)

try:
    line_count = 0
    for line in sys.stdin:
        # Parse the log line and split it into components
        parts = line.split()
        if len(parts) >= 9:
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Check if the status code is valid
            if status_code in ["200", "301", "400",
                               "401", "403", "404", "405", "500"]:
                # Update the metrics
                total_file_size += file_size
                status_code_count[status_code] += 1
                line_count += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print(f"File size: {total_file_size}")
                for code in sorted(status_code_count):
                    print(f"{code}: {status_code_count[code]}")

except KeyboardInterrupt:
    # Handle Ctrl+C gracefully by printing the statistics one last time
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count):
        print(f"{code}: {status_code_count[code]}")
