clean:
	rm -rf books/* posts/*

generate:
	python3 ./goodreads-csv-to-markdown.py

.PHONY: clean generate