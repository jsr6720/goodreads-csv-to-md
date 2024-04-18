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

American Hunter by Willie Robertson
William  Doyle 

https://www.goodreads.com/book/show/25110847

Bookshelves

Exclusive: did-not-finish

Bookshelves: did-not-finish

Binding/Format: Audiobook

## My Review 1/5

Didn't finish. Book was a collection of anecdotes about his personal life, uninteresting, and previous hunter's lives which barely scratched the surface of their rich history.<br/><br/>Moral: people who spend time outdoors are more 'rugged' than those who spend time indoors.

---

##### Author's Note

Generated using https://github.com/jsr6720/goodreads-csv-to-md script

##### Significant revisions

tags: { page.tags | join: ", " } <!-- todo move this somewhere -->

- { page.date | date_to_string: "ordinal", "US" } Originally published on [{ site.url }]({ site.url }) with uid { page.uid }

##### EOF/Footnotes
