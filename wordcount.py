#!/usr/bin/env python

import sys
from collections import Counter


def count_words(handle):

    word_counts = Counter()

    for line in handle:

        line = line.strip().lower().split(" ")
        line = [w for w in line if not w == '']

        for word in line:

            word = word.\
                rstrip("?").\
                rstrip("!").\
                rstrip(".").\
                rstrip(",")

            word_counts[word] += 1

    # reverse-sort word counts by how many items
    word_counts = word_counts.items()
    word_counts.sort(key=lambda x: x[1], reverse=True)

    for count, word in word_counts[:20]:
            print "{}: {}".format(word, count)


with open(sys.argv[1]) as handle:
    count_words(handle)
