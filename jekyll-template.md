---
layout: post
author: James Rowe
title:  "Detect Thoughts on '{Title}'"
date:   {jekyll-date} -0400
tags: book review {author-ln} {book-tags}
uid: {guid}
---

<!-- highly dependent on how you personally use jekyll templates, and how you want this to show up -->

## My Review {My Rating}/5

Detect Thoughts: {My Review}

### Date Read
{Date Read}

### Date Added
{Date Added}

## Goodreads book information

*{Title}* by {Author}
{Additional Authors}

https://www.goodreads.com/book/show/{Book Id}

Bookshelves: {Bookshelves}

---

##### Author's Note

Initial `md` Generated using https://github.com/jsr6720/goodreads-csv-to-md

{Author}, *{Title}*, {Additional Authors} {Publisher} {Year Published} ({Binding})[^1]

##### Significant revisions

tags: {{ page.tags | join: ", " }} <!-- todo move this somewhere -->

- {{ {jekyll-date} | date_to_string: "ordinal", "US" }} Convereted to jekyll markdown format 
- {{ page.date | date_to_string: "ordinal", "US" }} Originally published on [goodreads](https://www.goodreads.com)

##### EOF/Footnotes

[^1]: ISBN: {ISBN}