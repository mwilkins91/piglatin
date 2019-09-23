vowels = ['a', 'e', 'i', 'o', 'u', 'y']


def pigify(text):
    words = text.split(' ')
    piglatinWords = []

    for word in words:
        if (word[0] in vowels):
            pigWord = word + 'ay'
        else:
            pigWord = word[1:] + word[0] + 'ay'
        piglatinWords.extend([pigWord])
    return ' '.join(piglatinWords)


text = input('Give me a word or phrase:  ')
print('Your text in piglatin: ')
print(pigify(text))
