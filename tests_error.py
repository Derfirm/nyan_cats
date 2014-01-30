# -*- coding: utf-8 -*-

import time
import unittest

from rainbowrunners.runner import NyanCatRunner


class Tests(unittest.TestCase):
    pass


def test_generator():
    def test(self):
        time.sleep(0.15)
        raise NotImplementedError
    return test


for i in range(20):
    test_name = 'test_%s' % i
    test = test_generator()
    setattr(Tests, test_name, test)


suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
NyanCatRunner().run(suite)
