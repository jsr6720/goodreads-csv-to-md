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

John Adams by David McCullough
Empty 

https://www.goodreads.com/book/show/2203

Bookshelves

Exclusive: read

Bookshelves: biography, history

Binding/Format: Paperback

## My Review 5/5

### Date Read
2015/06/24

### Date Added
2016/05/31

My Thoughts: Amazing. The life of John Adams is certainly overlooked as a founding father. Could not be happier.<br/><br/>Narrative of a strong man whose defining characteristic was New England purity and integrity.<br/>Jon Adams was the defense attorney for the British soldiers from the Boston massacre, did more to advance the independence cause in congress than any other member. <br/><br/>Founder of the navy and first father-son presidential pair. So many good lessons from his life.

---

##### Author's Note

Generated using https://github.com/jsr6720/goodreads-csv-to-md script

##### Significant revisions

tags: { page.tags | join: ", " } <!-- todo move this somewhere -->

- { page.date | date_to_string: "ordinal", "US" } Originally published on [{ site.url }]({ site.url }) with uid { page.uid }

##### EOF/Footnotes
