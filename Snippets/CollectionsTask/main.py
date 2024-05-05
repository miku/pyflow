
import collections
import random

s = """
From the Python Website: Python is a high-level, general-purpose programming
language. Its design philosophy emphasizes code readability with the use of
significant indentation. 
"""

words = collections.defaultdict(set) 
freq = collections.Counter()
for word in s.split():
    freq[word] += 1
    if len(word) > 10:
        words["long"].add(word)
    elif len(word) < 5:
        words["short"].add(word)

for w, f in freq.most_common(n=3):
    print(w, f)

print("short words: {}".format(random.sample(words["short"], 3)))
print("long words: {}".format(random.sample(words["long"], 3)))
