import csv
import os
import sys

def count_rows_in_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        row_count = sum(1 for row in reader)
    return row_count

def count_files_in_directory(directory):
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

def validate_csv_output(csv_file, output_directory):
    expected_rows = count_rows_in_csv(csv_file)
    generated_files = count_files_in_directory(output_directory)
    
    if expected_rows == generated_files:
        print("Validation successful: Number of rows in CSV matches the number of output files in " + output_directory)
    else:
        print("Validation failed: Number of rows in CSV does not match the number of output files in " + output_directory)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validator.py <csv_file_path> <output_directory_path>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    output_directory_path = sys.argv[2]

    validate_csv_output(csv_file_path, output_directory_path)
