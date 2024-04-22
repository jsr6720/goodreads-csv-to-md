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

What Got You Here Won't Get You There by Marshall Goldsmith
Empty 

https://www.goodreads.com/book/show/84525

Bookshelves

Exclusive: read

Bookshelves: read-again, business, personal-development

Binding/Format: Paperback

## My Review 5/5

### Date Read
Empty

### Date Added
2016/05/31

My Thoughts: Empty

---

##### Author's Note

Generated using https://github.com/jsr6720/goodreads-csv-to-md script

##### Significant revisions

tags: { page.tags | join: ", " } <!-- todo move this somewhere -->

- { page.date | date_to_string: "ordinal", "US" } Originally published on [{ site.url }]({ site.url }) with uid { page.uid }

##### EOF/Footnotes
