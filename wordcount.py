# put your code here.
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

    for word, count in word_counts.iteritems():
        print word, count

count_words('test.txt')