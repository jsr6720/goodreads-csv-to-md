# goodreads-csv-to-md

Takes a Goodreads data export CSV and generates markdown files targeting custom jekyll md template and basic markdown.

### Moved personal commentary to jsr6720.github.io repository

[Goodreads CSV Import](https://github.com/jsr6720/jsr6720.github.io/blob/7baa2a416b2fc2273df83b6ebcdc30f036a43977/_posts/2024-04-22-goodreads-csv-import.md)

## Steps to generate md files

1. [Export your goodreads data](#export-of-goodreads-data) to csv and place in `goodreads-data` folder
2. Modify [basic template](/md-template.md) and/or [jekyll template](/jekyll-template.md) to your hearts content
3. run `make build`
    * If you're getting a `KeyError` it most likely means you have a misnamed `{header}` in your template. It also dislikes whitespace `{ header } !== {header}` 
4. Copy markdown output to new system of record

See [sample-output](/sample-output/) for a one off example showing links and special characters.

## Export of Goodreads data

The [goodreads_library_export_original.csv](./goodreads-data/goodreads-library-export-original.csv) was generated from [Account Settings Page](https://help.goodreads.com/s/article/How-do-I-get-a-copy-of-my-data-from-Goodreads). I discovered some data that was easier for me clean up via goodreads UI so I [re-exported](./goodreads-data/goodreads-library-export.csv) for use with this script. Specifically the deleting of books from the "Want to read" bookshelf.

## Limitations / Edge cases not worth programming in my dataset

There is no check on unique tite's so I prepend book id on the simple tempalte. See *Art of War* example in this content. From my own data set I only had 3 conflicts which I'll fix manually on `jekyll` side

```
# two books that both start with "Influence: <subtitle>" I'll rename manually
- /Users/jrowe/code/jsr6720/jsr6720.github.io/_posts/2017-02-08-influence.md
- /Users/jrowe/code/jsr6720/jsr6720.github.io/_posts/2018-07-06-influence.md

# should likely add 'translation' data or publication year(?) again one off will fix manually
- /Users/jrowe/code/jsr6720/jsr6720.github.io/_posts/2018-02-05-the-art-of-war.md
- /Users/jrowe/code/jsr6720/jsr6720.github.io/_posts/2018-02-08-the-art-of-war.md

# looks like I accidently added the "Hardcover" and "Audio CD" to my bookshelf. Will combine reviews and delete one.
- /Users/jrowe/code/jsr6720/jsr6720.github.io/_posts/2020-02-10-the-wright-brothers.md
- /Users/jrowe/code/jsr6720/jsr6720.github.io/_posts/2020-02-20-the-wright-brothers.md
```

## ChatGPT 3.5 assisted(led?) coding

To say that I wouldn't have completed this without ChatGPT 3.5 is an understatement. I probably could've cobbled together a python csv parser that generated basic templates but it would've been brute force and required clean up to publish each review via jekyll.

### ChatGPT3.5 especially shined in the following areas:

* `format(**bookDict)` I never would've guessed python dictionary could seed a template file :mind-blown:
* regular expression to match book and author goodreads link format to markdown link format
* resolving git merge conflicts when I was trying to track changes of the generated files but still changing file name patterns
* generation of Makefile targets and mapping to python execution paths

### Some limitations I was able to work through

* When I asked for a file name sanitize function it was happy to write a whole new function when a quick google search reccomends importing a library to handle this. When asked about its knowledge of packages it was aware and modified the code to reflect
* It briefly got hung up on the regex for goodreads special link format. At some point it thought that it was returning the matches as a string, but was not. I was able to get it working as I wanted
* not much in the way of error handling or package definition, but GitHub has its own opinion on this and I could ask GPT3.5 to add it

## Warning: very manual process

https://www.goodreads.com/api as of 2024 states there is no longer active support for api keys and directs to https://help.goodreads.com/s/article/Does-Goodreads-support-the-use-of-APIs which directs users to use the [account data export feature](#export-of-goodreads-data).

> As of December 8th 2020, Goodreads no longer issues new developer keys for our public developer API and plans to retire the current version of these tools. You can find more information 

For now I generate a goodreads URL using the `Book Id` column.

`https://www.goodreads.com/book/show/{Book Id}`

## Licenses

[CC0 1.0 Universal LICENSE](/LICENSE) Covers all written content in exports and resulting templates. This content was previously available on my public [goodreads](https://www.goodreads.com) account.

[MIT License](/CODE-LICENSE) Covers the code within this repo. [Heavy lifting by ChatGPT 3.5](/ChatGPT35-prompt-log.md)