import csv
import os
import argparse
import uuid
from datetime import datetime
from sanitize_filename import sanitize # pip3 install sanitize_filename

## count number csv rows and number files generated should match
## optional download book image
## some reviews have links to authors/books. need to parse those
### [a:Drucker Peter F|12008|Peter F. Drucker|https://d2arxad8u2l0g7.cloudfront.net/authors/1318472244p2/12008.jpg]
### [b:The 80/20 Principle: The Secret to Achieving More with Less|181206|The 80/20 Principle  The Secret to Achieving More with Less|Richard Koch|https://images.gr-assets.com/books/1437557431s/181206.jpg|175093]

# some flags for working with the script
config = {
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

def main():
    # more stuff being managed by Makefile..
    parser = argparse.ArgumentParser(description='Process some data.')
    parser.add_argument('--csv', type=str, help='Path to the goodreads export CSV file')
    args = parser.parse_args()

    if not args.csv:
        raise ValueError("Please provide the path to the CSV file using the --csv option.")
    
    if not os.path.exists(args.csv):
        raise FileNotFoundError(f"File '{args.csv}' not found.")
    
    # this should be handled by Makefile now.. 
    if not os.path.exists(config['basic-output-dir']):
        os.makedirs(config['basic-output-dir'])
    
    if not os.path.exists(config['jekyll-output-dir']):
        os.makedirs(config['jekyll-output-dir'])

    with open(args.csv, 'r', newline='', encoding=config['encoding']) as csvfile:
        goodreadsData = csv.reader(csvfile)
        headings = next(goodreadsData)  # Extracting headings from the first row

        # tbh this whole loop gives me the heebies.. but it works for now.
        for aBook in goodreadsData:

            # First convert row array to list of dictionaries with headings as keys
            bookDict = ({headings[i]: value for i, value in enumerate(aBook)})

            # stamp it
            bookDict["now-timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # I know jekyll doens't need uids.. but even in a flat file the id brings me comfort
            bookDict["guid"] = uuid.uuid4()

            # tagging by author last name assumes all valid data
            bookDict["author-ln"] = bookDict["Author"].split()[-1]

            # book tags, no commas needed
            bookDict["book-tags"] = bookDict["Bookshelves"].replace(',', '')

            # set a post date using 'Date Read', 'Date Added', now() in that order
            # assumes goodreads data export format YYYY/MM/DD :( and I hardeded EST -0400 in template https://xkcd.com/2867/
            bookDict["jekyll-date"] = datetime.strptime(bookDict["Date Read"] or bookDict["Date Added"], "%Y/%m/%d")

            # Read the template file
            with open('./md-template.md', 'r') as template_file:
                basic_template_content = template_file.read()
                # pretty print 'Empty' for basic template
                for key, value in bookDict.items():
                    if not value:  # Check if value is empty
                        bookDict[key] = "Empty"
            
            # Read the template file
            with open('./jekyll-template.md', 'r') as template_file:
                jekyll_template_content = template_file.read()

            # simple markdown file that works anywhere
            basic_populated_content = basic_template_content.format(**bookDict)
            
            filename = os.path.join(config['basic-output-dir'], getFileNameByTitle(aBook[headings.index('Title')]) + ".md")
            with open(filename, 'w', encoding=config['encoding']) as md_file:
                md_file.write(basic_populated_content)

            # this is the personalized jekyll post template
            jekyll_populated_content = jekyll_template_content.format(**bookDict)
            
            filename = os.path.join(config['jekyll-output-dir'], getFileNameForJekyll(headings, aBook) + ".md")
            with open(filename, 'w', encoding=config['encoding']) as md_file:
                md_file.write(jekyll_populated_content)

if __name__ == "__main__":
    main()
