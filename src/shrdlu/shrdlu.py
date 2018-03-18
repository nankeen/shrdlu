#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from .critical_values import vals


class Shrdlu(object):
    regex = re.compile(r'[a-zA-Z]')
    expected_f = {
        "a": 0.08167,
        "b": 0.01492,
        "c": 0.02782,
        "d": 0.04253,
        "e": 0.12702,
        "f": 0.02228,
        "g": 0.02015,
        "h": 0.06094,
        "i": 0.06966,
        "j": 0.00153,
        "k": 0.00772,
        "l": 0.04025,
        "m": 0.02406,
        "n": 0.06749,
        "o": 0.07507,
        "p": 0.01929,
        "q": 0.00095,
        "r": 0.05987,
        "s": 0.06327,
        "t": 0.09056,
        "u": 0.02758,
        "v": 0.00978,
        "w": 0.0236,
        "x": 0.0015,
        "y": 0.01974,
        "z": 0.00074,
    }

    def __init__(self, text):
        self.text = text.lower()
        self._frequencies = {}
        self.n = len(self.regex.findall(self.text))
        self.critical_values = vals
        self.v = len(self.regex.findall(self.text)) - 1

    @property
    def frequencies(self):
        if not self._frequencies:
            letters = self.regex.findall(self.text)
            for letter in letters:
                try:
                    self._frequencies[letter] += 1
                except KeyError:
                    self._frequencies[letter] = 1
        return self._frequencies

    def chi_squared(self):
        chi_squared_calc = 0
        expected = 0
        observed = 0
        self.v = 0
        for key, value in self.expected_f.items():
            expected += value * self.n
            try:
                observed += self.frequencies[key]
            except KeyError:
                observed += 0
            if expected >= 5:
                chi_squared_calc += (observed - expected) ** 2 / expected
                self.v += 1
                expected = 0
                observed = 0
        self.v -= 1
        return chi_squared_calc

    def test(self):
        chi = self.chi_squared()
        if self.v <= 0:
            return False
        if self.v >= len(self.critical_values):
            crit = self.critical_values[-1]
        else:
            crit = self.critical_values[self.v - 1]
        print(chi, crit)
        if chi < crit:
            return True
        else:
            return False
