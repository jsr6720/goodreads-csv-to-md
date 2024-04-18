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

Good Strategy/Bad Strategy: The Difference and Why It Matters by Richard P. Rumelt
Sean Runnette 

https://www.goodreads.com/book/show/13179689

Bookshelves

Exclusive: did-not-finish

Bookshelves: did-not-finish

Binding/Format: Audio CD

## My Review 1/5

Did not finish. Narration was just too dry. <br/><br/>Good strategy contains a kernel of 'obvious' truth.

---

##### Author's Note

Generated using https://github.com/jsr6720/goodreads-csv-to-md script

##### Significant revisions

tags: { page.tags | join: ", " } <!-- todo move this somewhere -->

- { page.date | date_to_string: "ordinal", "US" } Originally published on [{ site.url }]({ site.url }) with uid { page.uid }

##### EOF/Footnotes
