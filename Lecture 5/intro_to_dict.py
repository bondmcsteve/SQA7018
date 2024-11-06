student_grades = {"Alice": 85, "BoB": 90, "Charlie": 92}
print (student_grades)

if "BoB" in student_grades:
    print("BoB is in the dictionary")

sentences = ["Python is a great programming language",
             "I love programming in Python",
             "Python sets are great for finding unique elements",
             "Dictionaries in Python are very useful"]

#words = [word for sentence in sentences for word in sentence.split()]

words= []

for sentence in sentences:
    split_words = sentence.split()

    for word in split_words:
        words.append(word)

unique_words = set(words)

word_frequency = {word: words.count(word) for word in unique_words}

sorted_word_frequency = sorted(word_frequency.items(), key = lambda x: x[0], reverse = True)

for word, frequency in sorted_word_frequency:
    # print(word: frequency)