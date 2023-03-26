from service.word_count_service import word_count_service

import unittest

class TestWordCountService(unittest.TestCase):
    sample_text = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog again and again."
    
    def test_word_count_service_success(self):
        result, status_code = word_count_service(
            text=TestWordCountService.sample_text
        )
        self.assertEqual(status_code, 200)
        self.assertEqual(
            result, 
            {
                "the": 4,
                "quick": 2,
                "brown": 2,
                "fox": 2,
                "jumps": 2,
                "over": 2,
                "lazy": 2,
                "dog": 2,
                "again": 2,
                "and": 1
            }
        )
        
    def test_word_count_service_empty_text(self):
        result, status_code = word_count_service('')
        self.assertEqual(status_code, 400)
        self.assertEqual(result, 'Missing input text')
