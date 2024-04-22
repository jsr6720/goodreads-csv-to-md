---
layout: post
author: James Rowe
title:  "<<title-similiar-to-filename>>"
date:   <<date-added>>
tags: <<tags-csv>
uid: <<uid>>
---

<!-- highly dependent on how you personally use jekyll templates, and how you want this to show up -->

## Title

Aesop's Fables by Aesop
Jonathan Kent 

https://www.goodreads.com/book/show/8873903

Bookshelves

Exclusive: read

Bookshelves: classics, read-again

Binding/Format: Audio CD + ebook

## My Review 5/5

### Date Read
2015/07/14

### Date Added
2016/05/31

My Thoughts: Very fun listen. Didn't realize so many stories with morals were from so ancient a time.

---

##### Author's Note

Generated using https://github.com/jsr6720/goodreads-csv-to-md script

##### Significant revisions

tags: { page.tags | join: ", " } <!-- todo move this somewhere -->

- { page.date | date_to_string: "ordinal", "US" } Originally published on [{ site.url }]({ site.url }) with uid { page.uid }

##### EOF/Footnotes
