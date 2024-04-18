---
layout: post
author: James Rowe
title:  "<<title-similiar-to-filename>>"
date:   <<date-added>>
tags: <<tags-csv>
uid: <<uid>>
---

## Intro Heading

{Title}

---

##### Author's Note



##### Significant revisions

tags: {{ page.tags | join: ", " }} <!-- todo move this somewhere -->

- {{ page.date | date_to_string: "ordinal", "US" }} Originally published on [{{ site.url }}]({{ site.url }}) with uid {{ page.uid }}

##### EOF/Footnotes
