s = """
From the Python Website: Python is a high-level, general-purpose programming
language. Its design philosophy emphasizes code readability with the use of
significant indentation. 
"""

# ...

```

[...] collects basic metrics over the text:

* count how often each word (as is, no need to normalize) appears
* collect short words (e.g. 4 chars or shorter)
* collect long words (e.g. 11 chars or longer)

It can output the following:

* top 3 most common words
* a random sample (e.g. of 3) of the shortest and the longest words

```
the 2
Python 2
From 1

short words: ['code', 'of', 'Its']
long words: ['readability', 'high-level,', 'indentation.']