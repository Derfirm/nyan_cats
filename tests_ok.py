# -*- coding: utf-8 -*-

import time
import unittest
import sys
from runner import NyanCatRunner


class Tests(unittest.TestCase):
    pass


def test_generator():
    def test(self):
        time.sleep(0.1)
    return test


for i in range(50):
    test_name = 'test_%s' % i
    test = test_generator()
    setattr(Tests, test_name, test)


suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
NyanCatRunner().run(suite)
