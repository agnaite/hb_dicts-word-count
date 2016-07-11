# put your code here.
the_file = open('test.txt')

word_counts = {}

for line in the_file:
    list_per_line = line.rstrip().lower().split(" ")
    for word in list_per_line:
        word_counts[word] = word_counts.get(word, 0) + 1

for word, count in word_counts.iteritems():
    print word, count