import csv
import os
import sys

# chatGPT generated file. I tweaked error message.. 

def count_rows_in_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        row_count = sum(1 for row in reader)
    return row_count

def count_files_in_directory(directory):
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

def count_md_files_in_directory(directory):
    md_files = [name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name)) and name.endswith('.md')]
    return len(md_files)

def validate_csv_output(csv_file, output_directory):
    expected_rows = count_rows_in_csv(csv_file)-1 # remove header from count
    generated_files = count_md_files_in_directory(output_directory) # spent way too long looking for a .DS_Store file..
    
    if expected_rows == generated_files:
        print(f"Validation successful: Number of rows in CSV ({expected_rows}) matches the number of md files in directory {output_directory} ({generated_files})")
    else:
        print(f"Validation failed: Number of rows in CSV ({expected_rows}) does not match the number of md files in {output_directory} ({generated_files})")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validator.py <csv_file_path> <output_directory_path>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    output_directory_path = sys.argv[2]

    validate_csv_output(csv_file_path, output_directory_path)
