# -*- coding: utf-8 -*-

import math
import unittest

from utils import Colors, get_terminal_size

__all__ = (
    'NyanCatResult',
)


class BaseRainbowResult(unittest.TestResult):
    """A test result class that can print rainbow and awesome pet to a stream.
    """

    separator1 = '\033[{0}m{1:*^70}\033[0m'.format(Colors.SEPARATOR1, '')
    separator2 = '\033[{0}m{1:-^70}\033[0m'.format(Colors.SEPARATOR2, '')

    def __init__(self, stream=None, verbosity=None):
        super(BaseRainbowResult, self).__init__(
            stream=stream, verbosity=verbosity
        )
        self.stream = stream
        self.width = get_terminal_size()[0] * 0.8
        self.tick = False
        self.number_of_lines = 4
        self.trajectories = [[], [], [], []]
        self.pet_width = 11
        self.scoreboard_width = 5
        self.trajectory_width_max = self.width - self.pet_width
        self.rainbow_colors = self.generate_colors()
        self.color_index = 0

    def addSuccess(self, test):
        super(BaseRainbowResult, self).addSuccess(test)
        self.draw()

    def startTestRun(self):
        self.cursor_hide()

    def stopTestRun(self):
        for i in range(self.number_of_lines):
            self.stream.write('\n')
        self.cursor_show()

    def draw(self):
        self.append_rainbow()
        draw_methods = (
            self.draw_rainbow,
            self.draw_pet,
        )
        for method in draw_methods:
            method()
            self.cursor_up()

        self.tick = not self.tick

    def append_rainbow(self):
        segment = '_' if self.tick else '-'
        rainbowified = self.rainbowify(segment)

        for index in range(self.number_of_lines):
            trajectory = self.trajectories[index]
            if len(trajectory) >= self.trajectory_width_max:
                trajectory.pop(0)
            trajectory.append(rainbowified)

    def draw_rainbow(self):
        for trajectory in self.trajectories:
            self.stream.write('\033[{0}C'.format(self.scoreboard_width))
            self.stream.writeln(''.join(trajectory))

    def rainbowify(self, string):
        color = self.rainbow_colors[self.color_index % len(self.rainbow_colors)]
        self.color_index += 1
        return '\033[38;5;{0}m{1}\033[0m'.format(color, string)

    def generate_colors(self):
        pi3 = math.floor(math.pi / 3)
        n = lambda i: i * (1.0 / 6)
        r = lambda i: math.floor(3 * math.sin(n(i)) + 3)
        g = lambda i: math.floor(3 * math.sin(n(i) + 2 + pi3) + 3)
        b = lambda i: math.floor(3 * math.sin(n(i) + 4 + pi3) + 3)

        colors = [int(36 * r(i) + 6 * g(i) + b(i) + 16) for i in range(42)]
        return colors

    def cursor_up(self):
        self.stream.write('\033[{0}A'.format(self.number_of_lines))

    def cursor_hide(self):
        self.stream.write('\033[?25l')

    def cursor_show(self):
        self.stream.write('\033[?25h')


class NyanCatResult(BaseRainbowResult):
    def draw_pet(self):
        start_width = self.scoreboard_width + len(self.trajectories[0])
        color = '\033[{0}C'.format(start_width)

        self.stream.write(color)
        self.stream.writeln('_,------,')

        self.stream.write(color)
        padding = '  ' if self.tick else '   '
        self.stream.writeln('_|{0}/\\_/\\ '.format(padding))

        self.stream.write(color)
        padding = '_' if self.tick else '__'
        tail = '~' if self.tick else '^'
        self.stream.write('{0}|{1}{2} '.format(tail, padding, self.face()))
        self.stream.writeln()

        self.stream.write(color)
        padding = ' ' if self.tick else '  '
        self.stream.writeln('{0}""  "" '.format(padding))

    def face(self):
            return '( ^ .^)'
