# written almost exclusively by chatGPT 3.5 as I've never made a Makefile before

# Directories
BOOKS_DIR = books
POSTS_DIR = posts

# goodreads CSV file
CSV_FILE = ./goodreads-data/goodreads-library-export.csv

clean:
	rm -rf $(BOOKS_DIR)/* $(POSTS_DIR)/*

generate:
	mkdir -p $(BOOKS_DIR) $(POSTS_DIR)
	python3 ./goodreads-csv-to-markdown.py --csv $(CSV_FILE)

validate:
	python3 ./validate.py $(CSV_FILE) $(BOOKS_DIR)
	python3 ./validate.py $(CSV_FILE) $(POSTS_DIR)

build: clean generate validate

.PHONY: clean generate validate