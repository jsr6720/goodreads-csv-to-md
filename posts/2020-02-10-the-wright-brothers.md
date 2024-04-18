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

The Wright Brothers by David McCullough
Empty 

https://www.goodreads.com/book/show/22609391

Bookshelves

Exclusive: read

Bookshelves: history

Binding/Format: Hardcover

## My Review 5/5

Well written account of the turn of the century optimism the Wright brothers found themselves in. Also a great look at the 3rd hero Charlie Taylor. Fantastic story telling by McCullogh

---

##### Author's Note

Generated using https://github.com/jsr6720/goodreads-csv-to-md script

##### Significant revisions

tags: { page.tags | join: ", " } <!-- todo move this somewhere -->

- { page.date | date_to_string: "ordinal", "US" } Originally published on [{ site.url }]({ site.url }) with uid { page.uid }

##### EOF/Footnotes
