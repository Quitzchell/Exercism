import string
from collections import Counter

def count_words(sentence):
    cleaned_sentence = sentence
    for char in sentence:
        if char in string.punctuation and char != "'":
            cleaned_sentence = cleaned_sentence.replace(char, " ")

    words = []
    for word in cleaned_sentence.split():
        word = word.strip("'").lower()
        if word:
            words.append(word.strip("'").lower())

    return Counter(words)