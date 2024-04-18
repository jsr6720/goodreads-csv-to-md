import csv
import os
import json
from sanitize_filename import sanitize # pip3 install sanitize_filename

## use the jekyll template
## Bookshelves == tags
## titles can be unwiedly for a file name
## dates in (Date Read, Date Added)
## optional download book image
## some reviews have links to authors/books. need to parse those
### [a:Drucker Peter F|12008|Peter F. Drucker|https://d2arxad8u2l0g7.cloudfront.net/authors/1318472244p2/12008.jpg]
### [b:The 80/20 Principle: The Secret to Achieving More with Less|181206|The 80/20 Principle  The Secret to Achieving More with Less|Richard Koch|https://images.gr-assets.com/books/1437557431s/181206.jpg|175093]

# some flags for working with the script
config = {
    'map-empty-values-to-string-empty': True,
    'encoding': 'utf-8'
}

def main(csv_file):
    
    output_dir = "books"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(csv_file, 'r', newline='', encoding=config['encoding']) as csvfile:
        reader = csv.reader(csvfile)
        headings = next(reader)  # Extracting headings from the first row
        for row in reader:

            title = row[headings.index('Title')].strip()  # Extracting title from the row
            sanitized_title = sanitize(title)  # Sanitize the title for use as a filename

            # Read the template file
            with open('./md-template.md', 'r') as template_file:
                template_content = template_file.read()

            # Convert row array to list of dictionaries with headings as keys
            bookDict = ({headings[i]: value for i, value in enumerate(row)})
            
            # Convert empty values to "Empty"
            if config['map-empty-values-to-string-empty']:
                for key, value in bookDict.items():
                    if not value:  # Check if value is empty
                        bookDict[key] = "Empty"

            populated_content = template_content.format(**bookDict)
            
            filename = os.path.join(output_dir, f"{sanitized_title}.md")  # Using the sanitized title as the filename
            with open(filename, 'w', encoding=config['encoding']) as md_file:
                md_file.write(populated_content)

if __name__ == "__main__":

    default_filename = "goodreads_library_export.csv"
    csv_file = input(f"Enter file name to open (or press Enter for '{default_filename}'): ") or default_filename
    
    if os.path.exists(csv_file):
        main(csv_file)
        print("Conversion completed successfully!") # only an AI could be this cheerful about completing a task
    else:
        print(f"Error: File '{csv_file}' not found.")
