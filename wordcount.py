def wordcount(poem_file):
    poem = open(poem_file)

    words_count = {}

    for line in poem:
        line = line.rstrip()
        line = line.split(' ')

        for word in line:
            words_count[word] = words_count.get(word, 0) + 1

    for key in words_count:
        print(key, words_count[key])

    poem.close()

wordcount('twain.txt')


