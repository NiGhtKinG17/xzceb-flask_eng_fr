import unittest
from translator import englishToFrench, frenchToEnglish

class TestE2F(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench(None), None)
        self.assertEqual(englishToFrench("Hello"),"Bonjour")

class TestF2E(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish(None), None)
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")

unittest.main()