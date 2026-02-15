"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the "un" prefix."""
    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a prefixed string."""
    prefix = vocab_words[0]
    for index, word in enumerate(vocab_words[1:]):
        vocab_words[index + 1] = prefix + word

    return " :: ".join(vocab_words)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind."""
    root = word[:-4]
    if root[-1] == "i":
        return root[:-1] + "y"

    return root


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb."""
    word = sentence.split()[index]
    if word[-1] == ".":
        return word[:-1] + "en"

    return word + "en"
