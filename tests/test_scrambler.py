import os
import string
import sys
import unittest


sys.path.insert(0, os.path.join("..", "text_scrambler"))

import dictionaries
from text_scrambler import Scrambler


class TestScrambler(unittest.TestCase):
    s = Scrambler()
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

    def test_wrong_level(self):
        for wrong_level in [0, 5, 10, str, "hard"]:
            with self.subTest(msg=f"wrong level is {wrong_level}"):
                self.assertRaises(ValueError, self.s.scramble, self.text, wrong_level)

    def test_scramble(self):
        for level in [1, 2, 3, 4]:
            new_text = self.s.scramble(self.text, level)
            self.assertNotEqual(new_text, self.text)

    def test_generate(self):
        n_times = 1000
        for level in [1, 2, 3, 4]:
            res = self.s.generate(self.text, n=n_times, level=level)
            self.assertEqual(len(set(res)), len(res))


unittest.main()
