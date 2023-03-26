from service.bigram_service import bigram_service

import unittest

class TestBigramAnalysisService(unittest.TestCase):
    sample_text = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog again and again."
    
    def test_bigram_service_success(self):
        result, status_code = bigram_service(
            text=TestBigramAnalysisService.sample_text
        )
        self.assertEqual(status_code, 200)
        self.assertEqual(
            result,
            [
                ["quick", "the"],
                ["brown", "quick"],
                ["brown", "fox"],
                ["fox", "jumps"],
                ["jumps", "over"],
                ["over", "the"],
                ["lazy", "the"],
                ["dog", "lazy"],
                ["again", "and"],
                ["again", "dog"]
            ]
        )
    
    def test_bigram_service_empty_text(self):
        result, status_code = bigram_service('')
        self.assertEqual(status_code, 400)
        self.assertEqual(result, 'Missing input text')