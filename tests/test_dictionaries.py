import os
import string
import sys
import unittest


sys.path.insert(0, os.path.join("..", "text_scrambler"))

import dictionaries


class TestDictionaries(unittest.TestCase):

    text = string.ascii_lowercase

    def test_length_latin_dict(self):
        self.assertTrue(len(dictionaries.dic_latin_2_greek) > 10)
        self.assertTrue(len(dictionaries.dic_latin_2_cyrillic) > 10)
        self.assertTrue(len(dictionaries.dict_latin) > 10)

    def test_latin_chars(self):
        for dict_ in [
            dictionaries.dic_latin_2_greek,
            dictionaries.dic_latin_2_cyrillic,
        ]:
            for char in self.text:
                if char not in dict_:
                    continue
                for different_letter in dict_[char]:
                    self.assertNotEqual(char, different_letter)


unittest.main()
