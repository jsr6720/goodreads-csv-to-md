---
layout: post
author: James Rowe
title: "Quick Thoughts on {Title}"
date: {jekyll-date} -0400
category: review
tags: book {book-tags}
uid: {guid}
---

{Author}, *[{Title}](https://www.goodreads.com/book/show/{Book Id})*, {Additional Authors} {Publisher} {Year Published} ({Binding}) ISBN: {ISBN}

## My Review {My Rating}/5

{review-parsed}

### Date Read
{Date Read}

### Date Added
{Date Added}

---

### Significant revisions

- {{{{ "{now-timestamp}" | date_to_string: "ordinal", "US" }}}} Converted to jekyll markdown format and copied to personal site using <https://github.com/jsr6720/goodreads-csv-to-md>
- {{{{ page.date | date_to_string: "ordinal", "US" }}}} Originally published on [goodreads](https://www.goodreads.com) Bookshelves: {Bookshelves}