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

{Title} by {Author}
{Additional Authors} 

https://www.goodreads.com/book/show/{Book Id}

Bookshelves

Exclusive: {Exclusive Shelf}

Bookshelves: {Bookshelves}

Binding/Format: {Binding}

## My Review {My Rating}/5

### Date Read
{Date Read}

### Date Added
{Date Added}

My Thoughts: {My Review}

---

##### Author's Note

Generated using https://github.com/jsr6720/goodreads-csv-to-md script

##### Significant revisions

tags: {{ page.tags | join: ", " }} <!-- todo move this somewhere -->

- {{ page.date | date_to_string: "ordinal", "US" }} Originally published on [{{ site.url }}]({{ site.url }}) with uid {{ page.uid }}

##### EOF/Footnotes
