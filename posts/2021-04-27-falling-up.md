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

Falling Up by Shel Silverstein
Empty 

https://www.goodreads.com/book/show/30120

Bookshelves

Exclusive: read

Bookshelves: poetry, childhood-favorite

Binding/Format: Hardcover

## My Review 5/5

Revisiting another childhood favorite. Kids loved it. Great reminder of the fun things in life.

---

##### Author's Note

Generated using https://github.com/jsr6720/goodreads-csv-to-md script

##### Significant revisions

tags: { page.tags | join: ", " } <!-- todo move this somewhere -->

- { page.date | date_to_string: "ordinal", "US" } Originally published on [{ site.url }]({ site.url }) with uid { page.uid }

##### EOF/Footnotes
