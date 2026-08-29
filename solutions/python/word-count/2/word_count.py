import string
from collections import Counter

def count_words(sentence):
    cleaned_sentence = sentence
    for char in string.punctuation:
        if char != "'":
            cleaned_sentence = cleaned_sentence.replace(char, " ")

    words = []
    for word in cleaned_sentence.split():
        clean_word = word.strip("'").lower()
        if clean_word:
            words.append(clean_word)

    return Counter(words)