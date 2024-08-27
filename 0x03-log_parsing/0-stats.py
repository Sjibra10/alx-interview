#!/usr/bin/python3
import sys


def log_parsing(line):
    try:
        parts = line.split('"')
        ip_address = parts[0].strip()
        date = parts[1].split()[0].strip('[')
        status_code = int(parts[2].split()[1])
        file_size = int(parts[2].split()[-1])
        return ip_address, date, status_code, file_size
    except IndexError:
        return None

def compute_metrics(log_lines):
    """
    Computes metrics based on the parsed log lines.

    Args:
        log_lines (list): List of log lines.

    Returns:
        dict: A dictionary containing computed metrics.
    """
    total_requests = 0
    total_file_size = 0
    unique_ips = set()

    for line in log_lines:
        parsed_data = parse_log_line(line)
        if parsed_data:
            ip_address, _, _, file_size = parsed_data
            total_requests += 1
            total_file_size += file_size
            unique_ips.add(ip_address)

    metrics = {
        "total_requests": total_requests,
        "total_file_size": total_file_size,
        "unique_ips": len(unique_ips)
    }
    return metrics


