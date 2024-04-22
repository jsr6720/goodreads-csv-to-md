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

Letter from Birmingham Jail by Martin Luther King Jr.
Dion Graham 

https://www.goodreads.com/book/show/17623918

Bookshelves

Exclusive: read

Bookshelves: Empty

Binding/Format: Audio CD

## My Review 5/5

### Date Read
2018/09/06

### Date Added
2018/09/06

My Thoughts: Nice to listen to the source material.

---

##### Author's Note

Generated using https://github.com/jsr6720/goodreads-csv-to-md script

##### Significant revisions

tags: { page.tags | join: ", " } <!-- todo move this somewhere -->

- { page.date | date_to_string: "ordinal", "US" } Originally published on [{ site.url }]({ site.url }) with uid { page.uid }

##### EOF/Footnotes
