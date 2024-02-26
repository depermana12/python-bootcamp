sentence = input()

words_list = sentence.split(' ')
print(words_list)

count_words = {word: words_list.count(word) for word in words_list}

print(count_words)
