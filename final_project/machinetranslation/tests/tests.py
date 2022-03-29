import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test_null(self):
        self.assertEqual(english_to_french(" "), " ")

    def test_hello(self):
        self.assertEqual(english_to_french("hello").lower(), "bonjour")


class TestF2E(unittest.TestCase):
    def test_null(self):
        self.assertEqual(french_to_english(" "), " ")

    def test_hello(self):
        self.assertEqual(french_to_english("bonjour").lower(), "hello")


if __name__ == '__main__':
    unittest.main()
