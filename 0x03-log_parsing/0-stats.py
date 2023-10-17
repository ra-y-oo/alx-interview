import sys

# Define the metrics to compute
total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}

# Read stdin line by line
line_count = 0
for line in sys.stdin:
    line_count += 1

    # Split the line into fields
    fields = line.split()

    # Skip invalid lines
    if len(fields) != 5:
        continue

    # Parse the fields
    ip_address = fields[0]
    date = fields[1]
    method = fields[2]
    uri = fields[3]
    status_code = fields[4]

    # Validate the status code
    try:
        status_code = int(status_code)
    except ValueError:
        continue

    # Increment the status code count
    status_code_counts[status_code] += 1

    # Compute the total file size
    file_size = int(fields[4])
    total_file_size += file_size

    # Print statistics every 10 lines and/or a keyboard interruption (CTRL + C)
    if line_count % 10 == 0 or sys.stdin.isatty():
        print("Total file size: File size:", total_file_size)
        for status_code in sorted(status_code_counts):
            count = status_code_counts[status_code]
            if count > 0:
                print(f"{status_code}: {count}")

