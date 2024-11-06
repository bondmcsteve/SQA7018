# Based on Problem P4.2.2

from urllib.request import urlretrieve

# Begin by extracting the file into the script
f = open("2701-0.txt")
#print(f.read())

#Initialise word
words = []

what = set(f.read())
print(what)

# for sentence in f.read():
#     split_words = sentence.split()
#
#     for word in split_words:
#         words.append(word)

#unique_words = set(words)

#word_frequency = {word: words.count(word) for word in unique_words}

#sorted_word_frequency = sorted(word_frequency.items(), key = lambda x: x[0], reverse = False)

#print(unique_words)
#print(sorted_word_frequency)
#print(word: sorted_word_frequency)