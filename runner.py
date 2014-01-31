# -*- coding: utf-8 -*-

import sys
# import time
import unittest
# import warnings



from result import NyanCatResult
# from utils import Colors

__all__ = (
    'NyanCatRunner',
)


class BaseRainbowRunner(object):
    resultclass = None

    def __init__(self, stream=None):
        if stream is None:
            stream = sys.stderr
        self.stream = unittest.runner._WritelnDecorator(stream)

    def _makeResult(self):
        return self.resultclass(stream=self.stream,)

    def run(self, test):
        result = self._makeResult()
        startTestRun = getattr(result, 'startTestRun', None)
        if startTestRun is not None:
            startTestRun()
        test(result)
        stopTestRun = getattr(result, 'stopTestRun', None)
        if stopTestRun is not None:
            stopTestRun()
        ## line separator as _________
        # if hasattr(result, 'separator2'):
        #     self.stream.writeln(result.separator2)
        run = result.testsRun
        # answer after _____
        # self.stream.writeln('\033[{0}mRan {1} test{2} in {3:.3}s\033[0m'.format(
            # Colors.RESULT, run, run != 1 and 's' or '', ##time_taken
        # ))
        self.stream.writeln()
        return result


class NyanCatRunner(BaseRainbowRunner):
    resultclass = NyanCatResult
