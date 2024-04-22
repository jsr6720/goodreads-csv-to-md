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

The Phantom Tollbooth by Norton Juster
Jules Feiffer, Maurice Sendak 

https://www.goodreads.com/book/show/378

Bookshelves

Exclusive: read

Bookshelves: childhood-favorite, fiction

Binding/Format: Paperback

## My Review 5/5

### Date Read
2021/04/03

### Date Added
2021/04/03

My Thoughts: A fun whimsical look at mature childhood books. Classic. 

---

##### Author's Note

Generated using https://github.com/jsr6720/goodreads-csv-to-md script

##### Significant revisions

tags: { page.tags | join: ", " } <!-- todo move this somewhere -->

- { page.date | date_to_string: "ordinal", "US" } Originally published on [{ site.url }]({ site.url }) with uid { page.uid }

##### EOF/Footnotes
