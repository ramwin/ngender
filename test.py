#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-02-26 16:48:07


import unittest
from ngender import guess


class MyTest(unittest.TestCase):

    def test_name(self):
        self.assertEqual(guess("李胜男")[0], 'female')
        self.assertEqual(guess("李胜")[0], 'male')
        self.assertEqual(guess("李男")[0], 'male')
        self.assertEqual(guess("李招弟")[0], 'female')
        self.assertEqual(guess("李招")[0], 'male')
        self.assertEqual(guess("李弟")[0], 'male')


if __name__ == "__main__":
    unittest.main()
