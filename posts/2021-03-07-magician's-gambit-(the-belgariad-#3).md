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

Magician's Gambit (The Belgariad #3) by David Eddings
Empty 

https://www.goodreads.com/book/show/44688

Bookshelves

Exclusive: read

Bookshelves: fantasy, childhood-favorite

Binding/Format: Mass Market Paperback

## My Review 5/5

Picked this up from my childhood pile to give it a reread. I found all my favorite characters. One thing I do wish I could un-see though is all the similarities to other works of fiction in the same time period. All and all a great trip back in time.

---

##### Author's Note

Generated using https://github.com/jsr6720/goodreads-csv-to-md script

##### Significant revisions

tags: { page.tags | join: ", " } <!-- todo move this somewhere -->

- { page.date | date_to_string: "ordinal", "US" } Originally published on [{ site.url }]({ site.url }) with uid { page.uid }

##### EOF/Footnotes