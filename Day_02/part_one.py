# Function to determine if a report is safe
def is_safe(report):
    # Check if the levels are either all increasing or all decreasing
    increasing = all(report[i + 1] - report[i] > 0 for i in range(len(report) - 1))
    decreasing = all(report[i] - report[i + 1] > 0 for i in range(len(report) - 1))

    if not (increasing or decreasing):
        return False

    # Check if adjacent levels differ by at least 1 and at most 3
    differences_valid = all(1 <= abs(report[i + 1] - report[i]) <= 3 for i in range(len(report) - 1))

    return differences_valid

# Main function to process input data and count safe reports
def count_safe_reports(input_file):
    safe_count = 0

    # Read the input file
    with open(input_file, 'r') as file:
        for line in file:
            # Convert each line to a list of integers
            report = list(map(int, line.strip().split()))

            # Check if the report is safe
            if is_safe(report):
                safe_count += 1

    return safe_count

# Input file containing the unusual data
input_file = "input.txt"

# Count and print the number of safe reports
print("Number of safe reports:", count_safe_reports(input_file))
