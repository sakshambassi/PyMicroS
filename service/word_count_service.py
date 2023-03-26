from collections import Counter, OrderedDict
from util.process_input import remove_non_alphanumeric

import logging

def word_count_service(text):
    """ counts word in given sequence of text

    Args:
        text (str): input sequence

    Returns:
        OrderedDict: dict of key=word and val=count of the word
    """
    if not text:
        return jsonify(error='Missing input text'), 400

    words = remove_non_alphanumeric(text).lower().split()
    logging.info(f'Fetched words from input text={words}')

    if len(words) < 1:
        return jsonify(error='Input text must contain at least one word'), 400

    count = Counter(words)
    return OrderedDict(count.most_common())
