---
layout: post
author: James Rowe
title:  "Detect Thoughts on '{short-title}'"
date:   {jekyll-date} -0400
tags: book review {author-ln} {book-tags}
uid: {guid}
---

<!-- highly dependent on how you personally use jekyll templates, and how you want this to show up -->
<!-- escape any jekyll keys with double brackets -->

## My Review {My Rating}/5

{review-parsed}

### Date Read
{Date Read}

### Date Added
{Date Added}

## Goodreads book information

*{Title}* by {Author}

https://www.goodreads.com/book/show/{Book Id}

Bookshelves: {Bookshelves}

---

##### Author's Note

Initial `md` Generated using https://github.com/jsr6720/goodreads-csv-to-md

{Author}, *{Title}*, {Additional Authors} {Publisher} {Year Published} ({Binding})[^1]

##### Significant revisions

tags: {{{{ page.tags | join: ", " }}}} <!-- todo move this somewhere -->

- {{{{ {now-timestamp} | date_to_string: "ordinal", "US" }}}} Converted to jekyll markdown format and copied to personal site
- {{{{ page.date | date_to_string: "ordinal", "US" }}}} Originally published on [goodreads](https://www.goodreads.com)

##### EOF/Footnotes

[^1]: ISBN: {ISBN}