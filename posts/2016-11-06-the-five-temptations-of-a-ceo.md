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

The Five Temptations of a CEO by Patrick Lencioni
Empty 

https://www.goodreads.com/book/show/49146

Bookshelves

Exclusive: read

Bookshelves: Empty

Binding/Format: Hardcover

## My Review 5/5

Good quick read. Very compelling narrative and quick to get to the point. 

---

##### Author's Note

Generated using https://github.com/jsr6720/goodreads-csv-to-md script

##### Significant revisions

tags: { page.tags | join: ", " } <!-- todo move this somewhere -->

- { page.date | date_to_string: "ordinal", "US" } Originally published on [{ site.url }]({ site.url }) with uid { page.uid }

##### EOF/Footnotes
