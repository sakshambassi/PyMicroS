from collections import Counter
from util.process_input import (
    text_2_words_list,
    words_list_2_bigrams
)

import logging

def bigram_service(text):
    """ bigram service
    Assumptions:
    - assuming bigrams only exist in per sentence
    - assuming words' order doesn't matter in bigrams

    Args:
        text (str): input string

    Returns:
        list: list of tuples of bigrams
    """
    if not text:
        return 'Missing input text', 400

    if type(text) != str:
        return 'Text input should be string', 400

    try:
        words_list = text_2_words_list(text)
        logging.info(f'Successfully splitted words of all sentences.')
    except Exception as e:
        return f'Bad request: {e}', 400

    try:
        bigrams = words_list_2_bigrams(words_list)
        logging.info(f'Found bigrams = {bigrams}')
    except Exception as e:
        return f'Bad request: {e}', 400
    
    counter = Counter(bigrams)
    logging.info(f'Counter of bigrams = {counter}')
    
    return [[bigram[0][0], bigram[0][1]] for bigram in counter.most_common()], 200
