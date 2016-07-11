# put your code here.
the_file = open('twain.txt')

word_counts = {}

for line in the_file:
    line = line.rstrip()
    list_per_line = line.split(" ")
    for word in list_per_line:
        word_counts[word] = word_counts.get(word, 0) + 1

for word, count in word_counts.items():
    print word, count