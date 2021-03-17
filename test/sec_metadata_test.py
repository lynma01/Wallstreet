import unittest
import sys
sys.path.append("..")

import sec_metadata

class TestMetadata(unittest.TestCase):

    def test1(self):
        text1 = "hello world"
        text2 = "hello world!"

        self.assertEqual(text1, text2)
