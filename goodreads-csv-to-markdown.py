import csv
import os
from datetime import datetime
from sanitize_filename import sanitize # pip3 install sanitize_filename

## Bookshelves == tags
## 'fixed'title length, but if starts with "The" I want to move it to the end, like "The 10X Rule" -> "10X Rule, The"
## dates in (Date Read, Date Added)
## optional download book image
## some reviews have links to authors/books. need to parse those
### [a:Drucker Peter F|12008|Peter F. Drucker|https://d2arxad8u2l0g7.cloudfront.net/authors/1318472244p2/12008.jpg]
### [b:The 80/20 Principle: The Secret to Achieving More with Less|181206|The 80/20 Principle  The Secret to Achieving More with Less|Richard Koch|https://images.gr-assets.com/books/1437557431s/181206.jpg|175093]

# some flags for working with the script
config = {
    'map-empty-values-to-string-empty': True,
    'goodreads-export-filename': 'goodreads_library_export.csv',
    'encoding': 'utf-8',
    'basic-output-dir': 'books',
    'jekyll-output-dir': 'posts'
}

def getFileNameByTitle(title):
    # for my limited dataset really long titles, or books with subtitles usually have a ":" in them
    result = sanitize(title.split(':')[0].strip())

    if result.lower().startswith('the'):
        # Slice out "the" from the beginning of the string
        return result[3:] + ", " + result[:3]
    else: 
        return result

def getFileNameForJekyll(headings, aBook):
    # follows a specific pattern of YYYY-MM-DD-title.md
    # Date Read or Date Added - I guess I could just string replace '/' -> '-'
    date_object = datetime.strptime((aBook[headings.index('Date Read')] or aBook[headings.index('Date Added')]), "%Y/%m/%d")

    # Format datetime object as YYYY-MM-DD string
    formatted_date = date_object.strftime("%Y-%m-%d")

    temp = formatted_date + "-" + sanitize(aBook[headings.index('Title')].split(':')[0].strip())

    return temp.replace(' ', '-').lower()

def main(csv_file):
    
    if not os.path.exists(config['basic-output-dir']):
        os.makedirs(config['basic-output-dir'])
    
    if not os.path.exists(config['jekyll-output-dir']):
        os.makedirs(config['jekyll-output-dir'])

    with open(csv_file, 'r', newline='', encoding=config['encoding']) as csvfile:
        goodreadsData = csv.reader(csvfile)
        headings = next(goodreadsData)  # Extracting headings from the first row
        for aBook in goodreadsData:

            # Read the template file
            with open('./md-template.md', 'r') as template_file:
                basic_template_content = template_file.read()
            
            # Read the template file
            with open('./jekyll-template.md', 'r') as template_file:
                jekyll_template_content = template_file.read()

            # Convert row array to list of dictionaries with headings as keys
            bookDict = ({headings[i]: value for i, value in enumerate(aBook)})
            
            # Convert empty values to "Empty"
            if config['map-empty-values-to-string-empty']:
                for key, value in bookDict.items():
                    if not value:  # Check if value is empty
                        bookDict[key] = "Empty"

            basic_populated_content = basic_template_content.format(**bookDict)
            
            filename = os.path.join(config['basic-output-dir'], getFileNameByTitle(aBook[headings.index('Title')]) + ".md")
            with open(filename, 'w', encoding=config['encoding']) as md_file:
                md_file.write(basic_populated_content)


            jekyll_populated_content = jekyll_template_content.format(**bookDict)
            
            filename = os.path.join(config['jekyll-output-dir'], getFileNameForJekyll(headings, aBook) + ".md")
            with open(filename, 'w', encoding=config['encoding']) as md_file:
                md_file.write(jekyll_populated_content)

if __name__ == "__main__":

    default_filename = config['goodreads-export-filename']
    csv_file = input(f"Enter file name to open (or press Enter for '{default_filename}'): ") or default_filename
    
    if os.path.exists(csv_file):
        main(csv_file)
        print("Conversion completed successfully!") # only an AI could be this cheerful about completing a task
    else:
        print(f"Error: File '{csv_file}' not found.")
