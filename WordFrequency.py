text_doc = open('sometext.txt', 'r')

txt_file = text_doc.read()

word_frequency = {}

for word in txt_file.split():
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print(word_frequency)