from services.bigram_service import bigram_service

import unittest

class TestBigramAnalysisService(unittest.TestCase):
    sample_text = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog again and again."
    
    def test_bigram_service_success(self):
        result = bigram_service(
            text=TestBigramAnalysisService.sample_text
        )
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
