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

The Book of Five Rings by Miyamoto Musashi
Shiro Tsujimura, William Scott Wilson 

https://www.goodreads.com/book/show/13151220

Bookshelves

Exclusive: read

Bookshelves: history

Binding/Format: Hardcover

## My Review 4/5

Focuses on the combat aspects of leadership, but has concepts as well.

---

##### Author's Note

Generated using https://github.com/jsr6720/goodreads-csv-to-md script

##### Significant revisions

tags: { page.tags | join: ", " } <!-- todo move this somewhere -->

- { page.date | date_to_string: "ordinal", "US" } Originally published on [{ site.url }]({ site.url }) with uid { page.uid }

##### EOF/Footnotes
