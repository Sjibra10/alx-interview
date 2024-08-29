#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_file_size = 0
status_code_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

def print_stats():
    """Prints the metrics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print("{}: {}".format(code, status_code_count[code]))

def signal_handler(sig, frame):
    """Handles the keyboard interrupt signal."""
    print_stats()
    sys.exit(0)

# Register signal handler for keyboard interrupt (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

line_count = 0

try:
    for line in sys.stdin:
        # Ensure the line matches the required format
        parts = line.split()
        if len(parts) < 7:
            continue

        try:
            # Extract file size and status code
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update metrics
            total_file_size += file_size
            if status_code in status_code_count:
                status_code_count[status_code] += 1

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            continue

    # Final stats when stdin ends
    print_stats()

except (KeyboardInterrupt, BrokenPipeError):
    print_stats()
    sys.exit(0)

