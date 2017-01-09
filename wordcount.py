the_file = open("test.txt")


word_count = {}

for line in the_file:
    line = line.rstrip().split(" ")

    for word in line:

        if word in word_count:
            word_count[word] += 1

        else:
            word_count[word] = 1

print word_count


