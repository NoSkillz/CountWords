__author__ = 'VerDe'


def count_words():
    f = open("input_file.txt", "r")
    temp_dictionary = {}
    for word in f.read().split():   # read file and split words
        if word not in temp_dictionary:
            temp_dictionary[word.lower()] = 1
        else:
            temp_dictionary[word.lower()] += 1
    return temp_dictionary
    f.close()

word_count = count_words()
print("Total words:", sum(word_count.values()))     # print the sum of the dictionary values
for k, v in word_count.items():  # key, value
    print(k, v)
