import csv
import os
import json
from sanitize_filename import sanitize # pip3 install sanitize_filename

## use the jekyll template
## Bookshelves == tags
## dates in (Date Read, Date Added)
## author and additional authors
## optional write to exclusive shelf
## optional add flag for spoilers ahead
## optional private notes(?)
## optional download book image
## goodreads link bookid

def convert_row_to_md(row, headings, excluded_columns):
    md_content = f"## {row[headings.index('Title')]}\n\n"  # Adding title as header two
    for i, field in enumerate(row):
        if headings[i] not in excluded_columns and headings[i] != 'My Review':
            md_content += f"**{headings[i]}:** {field}\n\n"
    if 'My Review' in headings:
        md_content += f"\n## My Review\n\n{row[headings.index('My Review')]}\n"
    return md_content

def main(csv_file):
    excluded_columns = ["Spoiler", "Private Notes", "Read Count", "Owned Copies", "Author l-f", "Book Id", "Additional Authors"]
    
    output_dir = "books"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headings = next(reader)  # Extracting headings from the first row
        for row in reader:

            md_content = convert_row_to_md(row, headings, excluded_columns)
            title = row[headings.index('Title')].strip()  # Extracting title from the row
            sanitized_title = sanitize(title)  # Sanitize the title for use as a filename
            filename = os.path.join(output_dir, f"{sanitized_title}.md")  # Using the sanitized title as the filename
            with open(filename, 'w', encoding='utf-8') as md_file:
                md_file.write(md_content)
            
            # Read the template file
            with open('./md-template.md', 'r') as template_file:
                template_content = template_file.read()

            # Convert row array to list of dictionaries with headings as keys
            bookDict = ({headings[i]: value for i, value in enumerate(row)})
            
            populated_content = template_content.format(**bookDict)
            filename = os.path.join(output_dir, f"{sanitized_title}.markdown")  # Using the sanitized title as the filename
            with open(filename, 'w', encoding='utf-8') as md_file:
                md_file.write(populated_content)

if __name__ == "__main__":

    default_filename = "goodreads_library_export.csv"
    csv_file = input(f"Enter file name to open (or press Enter for '{default_filename}'): ") or default_filename
    
    if os.path.exists(csv_file):
        main(csv_file)
        print("Conversion completed successfully!")
    else:
        print(f"Error: File '{csv_file}' not found.")
