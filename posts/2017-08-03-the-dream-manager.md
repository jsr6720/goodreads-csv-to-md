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

The Dream Manager by Matthew Kelly
David Slavin 

https://www.goodreads.com/book/show/1794345

Bookshelves

Exclusive: read

Bookshelves: Empty

Binding/Format: Audio CD

## My Review 4/5

Care about your people and yourself and they in turn will care about the business.

---

##### Author's Note

Generated using https://github.com/jsr6720/goodreads-csv-to-md script

##### Significant revisions

tags: { page.tags | join: ", " } <!-- todo move this somewhere -->

- { page.date | date_to_string: "ordinal", "US" } Originally published on [{ site.url }]({ site.url }) with uid { page.uid }

##### EOF/Footnotes
