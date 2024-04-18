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

What to Eat by Marion Nestle
Empty 

https://www.goodreads.com/book/show/75182

Bookshelves

Exclusive: read

Bookshelves: food, personal-development

Binding/Format: Hardcover

## My Review 5/5

This is a great look of HOW to go grocery shopping. With a look at mostly NY stores it offers a great insight in how best to shop and feed your body.

---

##### Author's Note

Generated using https://github.com/jsr6720/goodreads-csv-to-md script

##### Significant revisions

tags: { page.tags | join: ", " } <!-- todo move this somewhere -->

- { page.date | date_to_string: "ordinal", "US" } Originally published on [{ site.url }]({ site.url }) with uid { page.uid }

##### EOF/Footnotes
