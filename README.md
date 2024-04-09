# goodreads-csv-to-md

Takes a Goodreads CSV data export and generates markdown files targeting jekyll md template

They[citation needed](https://xkcd.com/285/) say the brain can't tell the difference between audio books and physical books, majority of this list was consumed via audioCD during my commute to/from work.

## Export of Goodreads data

Had fun tracking my books at [goodreads.com](https://www.goodreads.com) but I wanted to consolidate my data to the one true overlord MSFT and use it as content for my [personal site](https://jsrowe.com) hosted at [jsr6720.github.io](https://github.com/jsr6720/jsr6720.github.io).

The [goodreads_library_export_original.csv](./goodreads_library_export_original.csv) was generated from [Account Settings Page](https://help.goodreads.com/s/article/How-do-I-get-a-copy-of-my-data-from-Goodreads). I discovered some data that was easier for me clean up via goodreads UI so I [re-exported](./goodreads_library_export.csv) it for use with this script. Specifically the deleting of books from the "Want to read" bookshelf.

## Goodreads account data

Copied from the account settings/profile page. I joined in May 2016. Prior to this I was tracking books on some now lost google sheet stored on an old google drive account.

232 ratings (3.88 avg) with 219 reviews. I guess maybe I don't like what I pick.

FAVORITE GENRES: Biography, Business, Classics, History, Non-fiction, Philosophy, and Psychology

## Screenshot of stats

![](good-read-stats.png)

## Licenses

/LICENSE/ Covers all written content that was previously available on my public [goodreads](https://www.goodreads.com) account.

/CODE-LICENSE/ Covers the code within this repo. But it was written with heavy help from ChatGPT 3.5 and GitHub Copilot. Especially since I initailly wrote it in python a language I'm familiar with, but decided to try it as a ruby task since LLMs make it trivial to port small scripts.