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

Influence: Mastering Life's Most Powerful Skill by Kenneth G. Brown
Empty 

https://www.goodreads.com/book/show/40648831

Bookshelves

Exclusive: read

Bookshelves: business, psychology

Binding/Format: Audio CD

## My Review 5/5

Great overview of lots of influence classics. This is a great course that covers all the recent literature. 

---

##### Author's Note

Generated using https://github.com/jsr6720/goodreads-csv-to-md script

##### Significant revisions

tags: { page.tags | join: ", " } <!-- todo move this somewhere -->

- { page.date | date_to_string: "ordinal", "US" } Originally published on [{ site.url }]({ site.url }) with uid { page.uid }

##### EOF/Footnotes