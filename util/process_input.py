import re

def remove_non_alphanumeric(text: str) -> str:
    """ processes the string to remove comma, periods, question mark etc

    Args:
        text (str): input sequence

    Returns:
        str: processed input
    """
    return re.sub('[^0-9a-zA-Z]+', ' ', text)

def text_2_words_list(text: str) -> list:
    """ converts input text to words

    Args:
        text (str): input text

    Returns:
        list: list of list of words
    """
    # splitting into sentences
    sentences = text.split('.')
    
    # spliting each sentence into words
    for i, sentence in enumerate(sentences):
        if sentence == []:
            del sentence[i]
        else:
            sentences[i] = remove_non_alphanumeric(sentence).lower().split()
    return sentences

def words_list_2_bigrams(words_list: list) -> list:
    """ converts list of words to one list of bigrams

    Args:
        words_list (list): list of sequences of words

    Returns:
        list: list of tuples (bigrams)
    """
    bigrams = []
    for words in words_list:
        if words != []:
            bigrams.extend(list(zip(words, words[1:])))
    
    
    # sorting to remove duplicates without order
    bigrams = [tuple(sorted(bigram)) for bigram in bigrams]
    return bigrams