# put your code here.
import sys

def count_words(filename):
    the_file = open(filename)

    word_counts = {}

    for line in the_file:
        #line = line.rstrip('?')
        list_per_line = line.rstrip().lower().split(" ")
        # out = [c for c in list_per_line if c not in ('!','.',':', '?')]
        # print out
        for word in list_per_line:
            word = word.rstrip('?')
            word = word.rstrip('!')
            word = word.rstrip('.')
            word = word.rstrip(',')
            word_counts[word] = word_counts.get(word, 0) + 1

    the_file.close()

    word_counts = word_counts.items()
    
    count = 0
    for tpl in word_counts:
        word_counts[count] = list(tpl)
        word_counts[count].reverse()
        count += 1

    word_counts.sort()
    word_counts.reverse()

    for count, word in word_counts:
        print "{}: {}".format(word, count)

count_words(sys.argv[1])

