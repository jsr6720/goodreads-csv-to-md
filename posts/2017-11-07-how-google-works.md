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

How Google Works by Eric Schmidt
Jonathan Rosenberg, Alan Eagle, Holter Graham 

https://www.goodreads.com/book/show/20549465

Bookshelves

Exclusive: read

Bookshelves: business

Binding/Format: Audio CD

## My Review 4/5

A collection of short anecdotes about Google and its management practices.<br/><br/>Coined the phrase "smart-creative" which is the evolution of Drucker's "knowledge worker". These smart creatives drive company growth by turning technical insights into marketable products.<br/>

---

##### Author's Note

Generated using https://github.com/jsr6720/goodreads-csv-to-md script

##### Significant revisions

tags: { page.tags | join: ", " } <!-- todo move this somewhere -->

- { page.date | date_to_string: "ordinal", "US" } Originally published on [{ site.url }]({ site.url }) with uid { page.uid }

##### EOF/Footnotes
